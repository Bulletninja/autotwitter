from slistener import SListener
import time, tweepy, sys

consumer_key = ''
consumer_secret = ''
access_token = ""
access_token_secret = ""
auth     = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api      = tweepy.API(auth)
track = ['google']
listen = SListener(api)
stream = tweepy.Stream(auth, listen)
print("Streaming started...")
try:
    #stream.userstream('valenluis')
    #stream.filter(follow = ['9192512'])
    stream.filter(track=track, async=True)
except:
    print("error!")
    stream.disconnect()
