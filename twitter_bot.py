#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, os

argfile = str(sys.argv[1])

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(argfile, "r") as f:
    data = f.read().replace('\n', ' ')
text_list = data.split(".")

for line in text_list:
    api.update_status(status=line)
    time.sleep(500)
