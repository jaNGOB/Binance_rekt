import tweepy
import random
consumer_key = "WRjmCSLytntBdPW0th9ZHcKKK"
consumer_secret = "RdGL2JolhPR1aT6zyvj0TzsI8obygDcmRzpLu8Ane0hgqI8D1s"
#access_token = "AAAAAAAAAAAAAAAAAAAAAIUFNwEAAAAAU4q3zupw5yQaZdIFUvV%2BDxnUaR4%3D3eO20Lg3f1bFcE8Yo1HFfdfLSXGgORqD48lSQKKND42k8lgH13"
access_token = "1370006839270776836-md0iBjWYg6ZaYPuUivewXbrk31XA5f"
access_token_secret = "ziJh5hjIZLd4Gz2p7gT3zuk1lFKlbpMfOvoshK8nBfPa1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
f = open("tweets.txt")
print(f.read()) 

def get_data():
    pass
#the big bad function

def create_tweets():
    count, max_, total, biggest = get_data()
    f = open("tweets.txt")
    v = f.readlines()
    x = random.randrange(0,len(v)-1,1)
    text = v[x].format(count,total,max_)
    api.update_status(text)

