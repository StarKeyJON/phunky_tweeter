#!/usr/bin/env python

from config import *
import tweepy

auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler)

if __name__ == "__main__":
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
