import tweepy
import time
from datetime import datetime

twitter_accounts = [
{
    'consumer_key' :'fwSh1dSI2ZoVlgLhDJtSzNC7f',
    'consumer_key_secret' : 'i6DrUhGAhxqZTiYoCQOPkApCiMyFZjyPUM7TJZESdyN35kE3VK',
    'access_token' : '1082757433766875136-ZzU7Bc9szLyEDKB1Nh6VKRnVjs8Y33',
    'access_token_secret' : 'fgt4FnzwRaxUxKOLTxddy8ntxMnLsv0WcI5oxalo9glxl'
}]


consumer_key = twitter_accounts[0]['consumer_key']
consumer_key_secret = twitter_accounts[0]['consumer_key_secret']
access_token = twitter_accounts[0]['access_token']
access_token_secret = twitter_accounts[0]['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

usernames =  [
    # "AlhMahsa",
    "artingarmsirii",
    "Miss_Moloud1998",
    "Ma_Pournia",
    "_oket",
    "shahab_twt",
    "ali_bitarafan4",
    "zahra_dm",
    "Artourshah",
    "aseyedp",
    "EbneHava",
    "ayyaaaar",
    "AliRahimi1400",
    "nish_goon",
    "A_raefipur",
    "yaminpour",
    "haj_haydar",
    "TohidAzizi"
]

def get_user_tweets(user):
    latest_id = 2345871337164779521
    user_tweets = list()
    while True:
        tweets = api.user_timeline(user.id,trim_user=True, include_rts=True, max_id= latest_id)
        print(latest_id, user._json['id'],  user)
        1/0
        if len(tweets) == 0 or len(user_tweets) >= 3000:
            print('break by len', user.id, len(user_tweets))
            return user_tweets

        for tweet in tweets:
            user_tweets.append(tweet._json)
            created_date = datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            if created_date < datetime(year=2021, month=2, day=1):
                print('break byy date', user.id, len(user_tweets), created_date)
                return user_tweets
            # print(type(tweet._json['created_at']), created_date)
            # 1/0
            latest_id = tweet._json['id']
            # print(tweet)
            

  
for username in usernames:
    user = api.get_user(username)
    # api.home_timeline()
    print(len(get_user_tweets(user)))
    # print(len(tweets))

