import tweepy
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# from nltk import sent_tokenize, word_tokenize
# from nltk.stem.snowball import SnowballStemmer
# from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('english'))
import pandas as pd
import numpy as np
import re  
# import spacy
# nlp = spacy.load('en_core_web_lg')
from datetime import *

consumer_key = "Ie9GlyLg24Rnu1KV6aXkQvLPh"
consumer_secret = "njAvJEOhMicoxXs40OLtCtHvnB2TgA6jRwUYujtUo3v9Fb1ZXZ"
access_key = "794428634530361344-K73P7BxwHopfsfQ3aS2mbSf8lS2NaLC"
access_secret = "MwfrGvSKZ7ugeFBiC9vaYmYluEwe0anmugAuWP3DnFpHR"

def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)
    # Calling api
    api = tweepy.API(auth)
    # Empty Array
    tmp = []
    date=[]
    loc = []
    for tweet in tweepy.Cursor(api.user_timeline, id=username,since="2021-03-20", until="2021-03-25", rpp=100, result_type="recent", include_entities=True, include_rts=False,lang="en", tweet_mode='extended').items(100):
        # Appending tweets to the empty array tmp
        tmp.append(tweet.full_text)
        t1 = tweet.created_at
        date.append(t1.hour)
        loc.append(tweet.place)
    # Printing the tweets
    print(date)
    print(loc)
    print(len(loc))
    return(tmp)
    
# def get_tweets(username):
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_key, access_secret)
#     api = tweepy.API(auth)
#     tmp = []
#     hour = []
#     months = []
#     for tweet in tweepy.Cursor(api.user_timeline, id=username,result_type="recent", include_entities=True, exclude_replies=True, exclude_retweets=True, lang="en", tweet_mode='extended').items(100):
#         tmp.append(tweet.full_text)
#         time = tweet.created_at
#         print(tweet.place.name)
#         months.append(time.strftime("%x"))
#     return tmp, months

def get_hashtag(keyword):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    t = []
    dates=[]
    loc = []
    for tweet in tweepy.Cursor(api.search, q=keyword,since="2021-03-20", until="2021-03-25", rpp=100, result_type="recent", include_entities=True, include_rts=False, include_media=False,lang="en", tweet_mode='extended').items(50):
        t.append(tweet.full_text)
        t1= tweet.created_at
        dates.append(t1.hour)
        loc.append(tweet.place.name)
    print(t)
    print(dates)
    print(loc)
# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("tim_cook")
    