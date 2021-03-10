from binance_connect import BinanceWebsocket
import datetime
from signal import signal, SIGINT
from time import sleep
import pytz
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

nance_ws = BinanceWebsocket()

def handler(sig, frame):
	logger.info(" This is the end !")
	nance_ws.exit()
	exit(0)

def get_quotes(since):
	temp = nance_ws.quote(since)
	return(temp)

def main():
	first = True
	logger.info('Warming up the Engine')
	sleep(3)
	while nance_ws.ws.sock.connected:

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
