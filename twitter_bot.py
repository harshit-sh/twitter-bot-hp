#!/usr/bin/env python
# Author: Harshit Sharma <hsharma1205@gmail.com>
# License: MIT

import tweepy, time, sys, os

argfile = str(sys.argv[1])

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# method to get chunks of string to limit the size of
# tweets to 140 characters
def chunkString(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

with open(argfile, "r") as f:
    data = f.read()
text_list = data.split("\n")
text_list = filter(None, text_list) # Remove empty strings

for line in text_list:
    if len(line) > 140:
        tmp = list(chunkString(line, 140))
        for i in tmp:
            api.update_status(status=i)
    else:
        api.update_status(status=line)
    time.sleep(600)
