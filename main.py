import tweepy
from decouple import config
import services
import time


auth = tweepy.OAuthHandler(consumer_key=config('api_key'),consumer_secret=config('api_secret_key'),
access_token=config('access_token'),access_token_secret=config('access_token_secret'))

api = tweepy.API(auth=auth)

def postTweet():
    return api.update_status(services.createTweet())

def run():
    while True:
        postTweet()
        time.sleep(86400)
        postTweet()
        time.sleep(86400)

if __name__ == "__main__":
    run()
        

