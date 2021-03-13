"""
Binance websocket. This Object connects to the stream of forced orders 
which are orders Binance executes on behalf of the trader becuase they are being 
liquidated. 
Several subroutines are implemented as seen below.
"""

import asyncio
import json
import websocket
import logging
from threading import Thread
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class BinanceWebsocket:
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Initializing WebSocket.")
        
        self.logger.info("Connecting to Binance")
        self._connect()
        self.logger.info('Connected.')
        
        self.data = []

    def on_message(self, message) -> logging:
        """
        If we receive a message from binance, save it to the database for later access.

        :param message: json message from Binance.
        :return: None. Pass message to database.
        """
        message = json.loads(message)
        price = float(message['o']['p'])
        quantity = float(message['o']['q'])
        pair = str(message['o']['s'])

        self.logger.info('Boi got liquidated and lost {} USD trading {}!! F'.format(round(price*quantity,2), pair))

    def on_error(self, error):
        self.logger.info(error)

    def on_close(self):
        self.logger.info("### closed ###")

    def on_open(self):
        self.logger.info('Opened')

    def _connect(self):
        """
        Establish a connection to the forceOrder stream of Binance and define callback functions.
        """
        self.logger.debug("Starting thread")
        self.ws = websocket.WebSocketApp("wss://fstream.binance.com/ws/!forceOrder@arr",
                        on_message = self.on_message,
                        on_error = self.on_error,
                        on_close = self.on_close)

        self.ws.on_open = self.on_open
        
        self.wst = Thread(target=lambda: self.ws.run_forever())
        self.wst.setDaemon(True)
        self.wst.start()
        self.logger.debug("Started thread")
