# twitter_etl.py
import tweepy
import pandas as pd
from datetime import datetime
import s3fs
import config  # Import the config module

def run_twitter_etl():
    # Access Twitter API keys and secrets from config module
    access_key = config.ACCESS_KEY
    access_secret = config.ACCESS_SECRET
    consumer_key = config.CONSUMER_KEY
    consumer_secret = config.CONSUMER_SECRET

    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # Creating an API object
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweets = api.user_timeline(
        screen_name="@elonmusk",
        count=200,
        include_rts=False,
        tweet_mode="extended",
    )

    tweet_data = []
    for tweet in tweets:
        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": tweet.full_text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        tweet_data.append(refined_tweet)

    df = pd.DataFrame(tweet_data)
    df.to_csv("refined_tweets.csv", index=False)

if __name__ == "__main__":
    run_twitter_etl()
