#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slistener import SListener
from sqlalchemy import *
import pandas as pd
import time, tweepy, sys

def get_df(query):
    result = engine.execute(query)
    names = result.keys()
    df = pd.DataFrame(result.fetchall())
    df.columns = names
    return df

## authentication
consumer_key = '' ## put a valid Twitter username here
consumer_secret = '' ## put a valid Twitter password here
access_token = ''
access_token_secret = ''
#df = get_df("SELECT token, token_secret as secret FROM amigos")
#df = pd.DataFrame(list(zip(df.token, df.secret)))

auth     = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api      = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def retuit(tweetid, token_tuple):
    for tok in token_tuple:
        auth.set_access_token(tok[0],tok[1])
        api = tweepy.API(auth)
        api.get_status(tweetid).retweet()

def tuit(token_tuple, msg):
    auth.set_access_token(token_tuple[0],token_tuple[1])
    api = tweepy.API(auth)
    api.update_status(msg)

def responder(tweetid, token_tuple, msg):
    for tok in token_tuple:
        auth.set_access_token(tok[0],tok[1])
        api = tweepy.API(auth)
        api.update_status(msg, in_reply_to_status_id = tweetid)

def main():
    track = ['#oferta', '#oferton', '#descuento', '#descuentos', '#rebaja',
    '#rebajas', 'aprovecha oferta', 'aprovecha descuento', 'aprovecha barato']

    listen = SListener(api)
    stream = tweepy.Stream(auth, listen)

    print("Streaming started...")

    try:
        #stream.userstream('valenluis')
        #stream.filter(follow = ['9192512'])
        stream.filter(languages=["es"], track=track, async=True)
    except:
        print("error!")
        stream.disconnect()



if __name__ == '__main__':
    main()
    #df.apply(lambda x: retuit(706878198156427264, x))
    #for i in range(len(df)):
    #    tuit((df.ix[i][0],df.ix[i][1]), "excelente día")
