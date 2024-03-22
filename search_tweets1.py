from linebot import LineBotApi
from linebot.models import TextSendMessage
import tweepy
import json
import os

file = open("twitter_api.json")
info = json.load(file)

bearer_token = os.environ.get("BEARER_TOKEN")
CLIENT_ID = info["CLIENT_ID"]
CLIENT_ID_SECRET = info["CLIENT_ID_SECRET"]
BEARER_TOKEN = info["BEARER_TOKEN"]
USER_ID = info["USER_ID"]
ACCESS_TOKEN = info["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = info["ACCESS_TOKEN_SECRET"]

search_url = "https://api.twitter.com/2/tweets/search/recent"
LINE_USER_ID = info["LINE_USER_ID"]
CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = info["CHANNEL_SECRET"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN,endpoint=search_url)

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_ID_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
    )

def main():
        response = client.get_users_tweets(
                                        USER_ID,
                                        max_results=30
                                        )

        # By default, only the ID and text fields of each Tweet will be returned
        for tweet in response.data:
            messages = TextSendMessage(text = (str(tweet.text)))
            line_bot_api.push_message(LINE_USER_ID, messages = messages)                
            
if __name__ == "__main__":
    main()
