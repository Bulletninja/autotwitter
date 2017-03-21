#!/usr/bin/env python

from tweepy import StreamListener
import pandas as pd
import json, time, sys

class SListener(StreamListener):

    def on_status(self, status):
        text = status.text
        created = status.created_at
        retweeted = status.retweeted
        record = {'text': text, 'created_at': created, 'retweeted': retweeted}
        if not record['retweeted'] and 'RT @' not in record['text']:
            print(record)
            self.api.retweet(status.id)
        #self.api.retweet(status.id)
        #status.retweet()
        #print(status.id)
        #print(record) #See Tweepy documentation to learn how to access other fields
        #collection.insert(record)


    def on_error(self, status):
        print('Error on status', status)

    def on_limit(self, status):
        print('Limit threshold exceeded', status)

    def on_timeout(self, status):
        print('Stream disconnected; continuing...')
