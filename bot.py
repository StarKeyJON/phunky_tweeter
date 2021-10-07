#!/usr/bin/env python
# The ID of the PunkBot is : 879737099074887682

from config import *
import tweepy
import time


# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(token, token_secret)
  
# calling the api 
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())
  
# the ID of the user
userID = "879737099074887682"


# fetching the tweets and returning the result to the __main__ function
def tweet():
    tweets = api.user_timeline(screen_name=screen_name, 
                           # 200 is the maximum allowed count, we will only pull 1 at a time
                           # This stays well below the API limit, which I believe is about 300 requests per 15 minutes
                           count=1,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    return tweets


if __name__ == "__main__":  
    while True:
        x = 0

    # print(tweets)
        tweets = tweet()
        for i in tweets:
            t = tweets[x]
            punkID = t['id']
            times = t['created_at']
            text = (t['full_text'])
            # These commands will prompt to your terminal to display the current tweet info
            print(userID)
            print(times)
            print(text)
            x+=1
            var = text.split(" ")[1]
            print(var)
            cryptourl = f"https://twitter.com/cryptopunksbot/status/{punkID}"
            punkurl = f"https://rarible.com/token/0xf07468ead8cf26c752c676e43c814fee9c8cf402:{var}"

            with open("tweets.txt", "r+") as f:
                lines = f.readlines()
                
                print(lines)
                
                if lines[0] == times:
                    print("Status already updated...")
                    
                elif lines[0] != times:
                    print("Updating status...")
                    f.close()
                    with open("tweets.txt", "w") as f:
                        
                        f.write(f"{times}")
                        f.close()
                        api.update_status(f"Buy the Phunk {var}, {punkurl} \n Looking left on the right side of history. \n #CryptoPunks #CryptoPunk #CryptoPhunks #CryptoPhunksv2 @CryptoPhunksv2 @PhunkBot ", attachment_url=cryptourl)

            time.sleep(30)
