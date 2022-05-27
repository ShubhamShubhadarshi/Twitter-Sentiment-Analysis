from textblob import TextBlob
import tweepy
import sys

keys = open('keys.txt','r').read().splitlines()

api_key = keys[0]
api_key_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'narendra modi'
tweet_amount = 100

tweets = tweepy.Cursor(api.search,q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
negative = 0
neutral = 0

for tweet in tweets:
    final_tweet = tweet.text.replace('RT','')
    if final_tweet.startswith(' @'):
        position = final_tweet.index(':')
        final_tweet = final_tweet[position+2:]
    if final_tweet.startswith('@'):
        position = final_tweet.index(' ')
        final_tweet = final_tweet[position+1:]
    
    analysis = TextBlob(final_tweet)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += tweet_polarity

    

print("Polarity:",polarity)
print("Positive tweets:",positive)
print("Negative tweets:",negative)
print("Neutral tweets",neutral)
