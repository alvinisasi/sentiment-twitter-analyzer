import tweepy
from textblob import TextBlob

consumer_key = 'SVYSzgiWwYw5rRe9m4jgtIVOl'
consumer_key_secret = 'hCqETfDoZ5TEl1p0YMB2mN3bWLeN21VYFPxrbDa8i3EShbWTXZ'
access_token = '736424382-UGxibhQshssuMjo5LwpYH4fHHABmO8fMN70VW2Kd'
access_token_secret = 'WJAKQV0TnI7o9YbaYvyP4i46P4zTFNXK2GPrEpVsPmke4'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Jokowi')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print('Positive')
    elif analysis.sentiment[0]<0:
        print('Negative')
    else: 
        print('Neutral')