"""
Main function of the project. Running this file will create a connection to Binance using 
Websockets which in turn will create a connection to the Database.
Once started, this program runs forever until it encounters an error or CTRL+c is pressed.

April 2021
"""
import os
from binance_connect import BinanceWebsocket
from signal import signal, SIGINT
import configparser as cp
from time import sleep
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

config = cp.ConfigParser()
config.read('{}/credentials.ini'.format(os.path.abspath(os.getcwd())))
ws = BinanceWebsocket(config['DATABASE']['name'], int(config['DATABASE']['batch_size']))

def handler(sig, frame):
	"""
	Handler function which captures commands such as Ctrl+C to kill the program.

	:param frame: Keyboard input.
	:return: Exit the program and close the websocket.
	"""
	logger.info(" This is the end !")
	ws.on_close()
	exit(0)

def main():
	logger.info('Warming up the Engine')
	sleep(3)
	while ws.ws.sock.connected:
		pass

if __name__ == '__main__':
	signal(SIGINT, handler)
	main()
