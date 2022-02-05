import tweepy
import time

CONSUMER_KEY = '#####'
CONSUMER_SECRET = '#####'
ACCESS_KEY = '#########'
ACCESS_SECRET = '#########'

auth= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

posts = api.home_timeline()

for post in posts:
    
    time_posted = post._json['created_at']
    twittername = post.user.name
    twitterAccount = post.user.screen_name
    print(time_posted)
    print(twitterAccount + " - " + twittername)
    print(str(post.id) + " >> " + post.text)
    print("")
        
