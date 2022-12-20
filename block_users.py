#!/usr/bin/python3
import datetime
import requests
import tweepy
import sqlite3

# Use your preferred method to load and parse environment variables.

##AUTH
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)

##CLIENT
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True
)

##API Auth and Access
api = tweepy.API(auth)

##Elon Musk just because he gets like 1,000 followers a second
elon_id = '44196397'


##Get Followers
elon_users_data = client.get_users_followers(
    id=elon_id,
    max_results=40
    )

#DB connection
dbPath = 'database path'
con = sqlite3.connect(dbPath)
cur = con.cursor()

#INSERT INTO DB
for x in elon_users_data.data:
    cur.execute("INSERT INTO usrdata (uid,name,username) VALUES (?,?,?)", (x.id,x.name,x.username))
    con.commit()
con.close()

api_len = []
##Block the accounts
for i in elon_users_data.data:
    api.create_block(user_id=i.id)
    api_len.append(i.id)
