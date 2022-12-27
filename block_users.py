import os
import tweepy

##AUTH
auth = tweepy.OAuth1UserHandler(
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret'],
)


##CLIENT
client = tweepy.Client(
    bearer_token=os.environ['bearer_token'],
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret'],
    wait_on_rate_limit=True
)

api = tweepy.API(auth)

## any snowball type user id will work
user = '44196397'

## get 40 followers of user
user_data = client.get_users_followers(
    id=user,
    max_results=40
    )

## block the followers of user
for i in user_data.data:
    api.create_block(user_id=i.id)
