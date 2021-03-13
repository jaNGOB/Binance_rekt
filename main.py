from binance_connect import BinanceWebsocket
import datetime
from signal import signal, SIGINT
from time import sleep
import pytz
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ws = BinanceWebsocket()

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
	first = True
	logger.info('Warming up the Engine')
	sleep(3)
	while ws.ws.sock.connected:

		now = datetime.datetime.now(pytz.utc)
		
		if first:
			first = False

		try:
			since = now - datetime.timedelta(minutes=1)
			#btc = get_quotes(since)
			#print(btc)
		
		except Exception as e:
			logger.error(str(e))
			continue

if __name__ == '__main__':
	signal(SIGINT, handler)
	main()
