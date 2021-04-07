"""
This file reads data from a local QuestDB and creates a tweet. When providing the keys and secrets to the twitter account,
it will automatically tweet out the collected statistics in a predefined format.

April 2021
"""

import io
import os
import tweepy
import random
import requests
import configparser as cp
import pandas as pd


config = cp.ConfigParser()
config.read('{}/credentials.ini'.format(os.path.abspath(os.getcwd())))

consumer_key = config['TWITTER']['consumer_key']
consumer_secret = config['TWITTER']['consumer_secret']
access_token = config['TWITTER']['access_token']
access_token_secret = config['TWITTER']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_data():
    #query = ("select PAIR, sum(USDVALUE) as SUM, max(USDVALUE) as MAX, timestamp"
    #        +" from liqui sample by 1h;")
    #r = requests.get("http://localhost:9000/exp?query="+query)
    r = requests.get("http://localhost:9000/exp?query=SELECT * FROM {};".format(config['DATABASE']['name']))
    rawData = r.text
    df = pd.read_csv(io.StringIO(rawData), parse_dates=['timestamp'], index_col='timestamp')
    last = df.last('1H')

    return last.PAIR.count(), round(last.USDVALUE.max(), 2), round(last.USDVALUE.sum(), 2)
    

def create_tweets():
    count, max_, total = get_data()
    f = open("tweets.txt")
    v = f.readlines()
    #x = random.randrange(0,len(v)-1,1)
    text = v[0].format(count, total, max_)
    # print(text)
    api.update_status(text)

if __name__ == '__main__':
	create_tweets()