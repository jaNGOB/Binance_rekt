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
config.read('{}/credentials.ini'.format(os.path.dirname(os.path.abspath(__file__))))

consumer_key = config['TWITTER']['consumer_key']
consumer_secret = config['TWITTER']['consumer_secret']
access_token = config['TWITTER']['access_token']
access_token_secret = config['TWITTER']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_data():
    """
    This function does not need any inputs and rather just queries the database
    hostet on the localhost. The query is set up so it will receive the amount
    of entries in the last hour, the sum of losses and the maximum loss in the last
    hour which will be returned.

    :return: one integer and two floats. 
    """
    query = ("SELECT count() AS count, sum(USDVALUE) AS sum, max(USDVALUE) AS max "
            +"FROM liqui "
            +"WHERE timestamp > now() - 3600000000L;")
    r = requests.get("http://localhost:9000/exp?query="+query)
    rawData = r.text
    df = pd.read_csv(io.StringIO(rawData))

    return df['count'].values[0], round(df['max'].values[0], 2), round(df['sum'].values[0], 2)
    

def create_tweet():
    """
    This function does not need any inputs as it reads the necessary tweets from a file
    which is called tweets.txt. The format should stay the same as the insertion of the 
    data is standardized. There is also no ouput since the tweet itself is the final product 
    of this function.
    """
    count, max_, total = get_data()
    f = open('{}/tweets.txt'.format(os.path.dirname(os.path.abspath(__file__))))
    v = f.readlines()
    x = random.randrange(0,len(v)-1,1)
    text = v[x].format(count, total, max_)
    # print(text)
    api.update_status(text)

if __name__ == '__main__':
	create_tweet()