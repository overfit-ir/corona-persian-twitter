import tweepy
import accounts

twitter_accounts = accounts.twitter_accounts

consumer_key = twitter_accounts[0]['consumer_key']
consumer_key_secret = twitter_accounts[0]['consumer_key_secret']
access_token = twitter_accounts[0]['access_token']
access_token_secret = twitter_accounts[0]['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users_seen_count = dict()
users = dict()

latest_id = 2345871337164779521

while True:
    saerched_tweets = api.search(
        'کرونا', count=500, result_type='recent', max_id=latest_id)
    # print(len(saerched_tweets), saerched_tweets[-1])
    for tweet in saerched_tweets:
        id = tweet._json['id']
        if id > latest_id:
            print('wrong')
            # 1/0
        latest_id = id
        user = tweet._json['user']

        users_seen_count[user['id']] = users_seen_count.get(user['id'], 0) + 1
        users[user['id']] = user
    if len(users_seen_count) > 500:
        break

print(sorted(users_seen_count.items(), key=lambda item: item[1])[-10:])
