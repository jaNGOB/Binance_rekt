"""
This file reads data from a local QuestDB and creates a tweet. When providing the keys and secrets to the twitter account,
it will automatically tweet out the collected statistics in a predefined format.
"""

import io
import tweepy
import random
import requests
import pandas as pd


consumer_key = "WRjmCSLytntBdPW0th9ZHcKKK"
consumer_secret = "RdGL2JolhPR1aT6zyvj0TzsI8obygDcmRzpLu8Ane0hgqI8D1s"
#access_token = "AAAAAAAAAAAAAAAAAAAAAIUFNwEAAAAAU4q3zupw5yQaZdIFUvV%2BDxnUaR4%3D3eO20Lg3f1bFcE8Yo1HFfdfLSXGgORqD48lSQKKND42k8lgH13"
access_token = "1370006839270776836-md0iBjWYg6ZaYPuUivewXbrk31XA5f"
access_token_secret = "ziJh5hjIZLd4Gz2p7gT3zuk1lFKlbpMfOvoshK8nBfPa1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def get_data():
    #query = ("select PAIR, sum(USDVALUE) as SUM, max(USDVALUE) as MAX, timestamp"
    #        +" from liqui sample by 1h;")
    #r = requests.get("http://localhost:9000/exp?query="+query)
    r = requests.get("http://localhost:9000/exp?query=SELECT * FROM liqui;")
    rawData = r.text
    df = pd.read_csv(io.StringIO(rawData), parse_dates=['timestamp'], index_col='timestamp')
    last = df.last('1H')

    return last.PAIR.count(), last.USDVALUE.max(), last.USDVALUE.sum()
    

def create_tweets():
    count, max_, total = get_data()
    f = open("tweets.txt")
    v = f.readlines()
    #x = random.randrange(0,len(v)-1,1)
    text = v[0].format(count,total,max_)
    api.update_status(text)

if __name__ == '__main__':
	create_tweets()