from typing import List
import tweepy

from my_stream_listener import MyStreamListener

twitter_auth_keys = {
        'api': 'YOUR_API_KEY_HERE',
        'api_secret': 'YOUR_API_KEY_SECRET_HERE',
        'access_token': 'YOUR_ACCESS_TOKEN',
        'access_secret': 'YOUR_ACCESS_TOKEN_SECRET_HERE'
    }

auth = tweepy.OAuthHandler(
        twitter_auth_keys['api'],
        twitter_auth_keys['api_secret']
    )
auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_secret']
    )

api = tweepy.API(auth)

# Posts a tweet using the developer account
def post(message: str) -> None:
    tweet = message
    status = api.update_status(status=tweet)
    print(status.id)


# Gets the timeline
def get_timeline():
    timeline = api.home_timeline()
    for tweet in timeline:
        print("Tweet ID: " + tweet.id)
        print("Tweet:\n",tweet.text)



# Gets user's timeline
def get_user_timeline():
    timeline = api.user_timeline()
    for tweet in timeline:
        print("Tweet ID: " + tweet.id)
        print("Tweet:\n",tweet.text)

# Streams tweets with the given keywords
def stream(keywords: List[str]) -> None:
    myStreamListener = MyStreamListener()
    myStream.Stream(auth = api.auth,listener = myStreamListener)
    myStream.filter(keywords) 

