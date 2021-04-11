"""
This file connects to QuestDB and receives new liquidations.
These liquidations are then added to a current batch until the batch_size is reached.
Once it is reached, the whole batch gets pushed to the database using the 
influx_line_protocol.

April 2021
"""

from influx_line_protocol import Metric
import logging
import socket

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class DataBase(object):
    def __init__(self, name, batch_size):

        self.logger = logging.getLogger(__name__)

        # Initialize the metrics to be pushed into the database.
        self.metric = Metric(name) # Name of the database. If it doesnt exist, one will be created.
        self.str_metric = ""
        self.metrics = ""

        self.COUNTER = 0
        self.BATCH_SIZE = batch_size
        self.HOST = 'localhost'
        self.PORT = 9009

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))


    def close_sock(self):
        """Close the socket to the DB"""
        self.sock.close()

    def new_message(self, message):
        """
        This function receives a message from the websocket and temporarily 
        stores chosen values in a string. As soon as BATCH_SIZE is reached,
        the whole batch will be pushed into the database.

        :param message: decoded json message 
        """
        self.COUNTER += 1

        self.metric.with_timestamp(message['E']*1000*1000)
        self.metric.add_value('PRICE', float(message['o']['ap']))
        self.metric.add_value('QUANTITY', float(message['o']['q']))
        self.metric.add_value('USDVALUE', float(message['o']['q']) * float(message['o']['p']))
        self.metric.add_tag('PAIR', str(message['o']['s']))
        self.str_metric = str(self.metric)
        self.str_metric += "\n"
        self.metrics += self.str_metric

        if self.COUNTER == self.BATCH_SIZE:
            self.logger.info('Batch inserted into DB')
            self.COUNTER = 0
            bytes_metric = bytes(self.metrics, "utf-8")
            self.sock.sendall(bytes_metric)
            self.str_metric = ""
            self.metrics = ""
