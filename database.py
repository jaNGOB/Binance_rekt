from influx_line_protocol import Metric
import logging
import socket


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class DataBase(object):
    def __init__(self):

        self.logger = logging.getLogger(__name__)

        # Initialize the metrics to be pushed into the database.
        self.metric = Metric("liqui") # Name of the database. If it doesnt exist, one will be created.
        self.str_metric = ""
        self.metrics = ""

        self.counter = 0
        self.batch_size = 50
        self.HOST = 'localhost'
        self.PORT = 9009

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))


    def close_sock(self):
        self.sock.close()

    def new_message(self, message):
        self.counter += 1

        self.metric.with_timestamp(message['E']*1000*1000)
        self.metric.add_value('PRICE', float(message['o']['p']))
        self.metric.add_value('QUANTITY', float(message['o']['q']))
        self.metric.add_tag('PAIR', str(message['o']['s']))
        self.str_metric = str(self.metric)
        self.str_metric += "\n"
        self.metrics += self.str_metric

        if self.counter % 100 == 0:
            self.logger.info('Current count:{}'.format(self.counter))

        if self.counter % self.batch_size == 0:
            self.logger.info('finished')
            bytes_metric = bytes(self.metrics, "utf-8")
            self.sock.sendall(bytes_metric)
            self.str_metric = ""
            self.metrics = ""
