import accounts
from datetime import datetime
import tweepy
import networkx as nx
import time
rate_limit_counts = 0
accounts = accounts.twitter_accounts


def limit_handled(func, wait_min):
    global rate_limit_counts
    global current_api_index
    # global twitter_accounts
    global api
    # ret = func()
    # return ret
    while True:
        try:
            ret = func()
            return ret
        except tweepy.RateLimitError:
            rate_limit_counts += 1
            print('w8ing 15.5 minutes...', 'counter:',
                  rate_limit_counts, 'time:', datetime.now())
            time.sleep(15*60 + 30)
            # current_api_index = (current_api_index + 1) % 2
            # cai = current_api_index
            # auth = tweepy.OAuthHandler(accounts[cai]['consumer_key'], accounts[cai]['consumer_key_secret'])
            # auth.set_access_token(accounts[cai]['access_token'], accounts[cai]['access_token_secret'])
            # api = tweepy.API(auth)
            # api = apis[current_api_index]

            print('api changed tp ', current_api_index, api)

# consumer_key = 'fwSh1dSI2ZoVlgLhDJtSzNC7f'
# consumer_key_secret = 'i6DrUhGAhxqZTiYoCQOPkApCiMyFZjyPUM7TJZESdyN35kE3VK'
# access_token = '1082757433766875136-ZzU7Bc9szLyEDKB1Nh6VKRnVjs8Y33'
# access_token_secret = 'fgt4FnzwRaxUxKOLTxddy8ntxMnLsv0WcI5oxalo9glxl'


consumer_key = accounts['consumer_key']
consumer_key_secret = accounts['consumer_key_secret']
access_token = accounts['access_token']
access_token_secret = accounts['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)


G = nx.Graph()
api = tweepy.API(auth)
# apis = [api1, api2]

current_api_index = 0
# api = apis[current_api_index]
user = api.get_user('saeednamaki')
un_seen_users = dict()
seen_users = set()
id_to_username = dict()

print(user.screen_name)
print(user.followers_count, user.id)

un_seen_users[user.id] = 5
print('before', un_seen_users, seen_users)
i = 0
while len(un_seen_users) > 0:
    user_id = max(un_seen_users, key=un_seen_users.get)
    user = api.get_user(user_id)
    G.add_node(user_id)
    # print(len(user.friends(), api.get_friends_ids(user_id)))
    # for friend in tweepy
    for friend in limit_handled(user.friends, 15):  # user.friends():
        i += 1
        # print(i, friend.id)
        # G.add_node(friend.id)
        # print(friend.lang)
        G.add_edge(user_id, friend.id)
        if friend.id not in seen_users:
            un_seen_users[friend.id] = un_seen_users.get(friend.id, 0) + 1
        # print(friend.screen_name, friend.id, friend)
        if len(seen_users) % 15 == 0:
            nx.write_graphml(G, "G.graphml")

    # print('dasdaß')
    del un_seen_users[user_id]
    seen_users.add(user_id)
    print('after', len(seen_users), len(un_seen_users), 'i=', i)
    print('G', len(G.nodes), len(G.edges))

print('after', un_seen_users, seen_users)
print('G', G.nodes, G.edges)


# for friend in user.friends():
#     ids.append(friend.id)
#     print(friend.screen_name, friend.id, friend)

# print(api.lookup_users(ids)[0])
# api.lookup_friendships
# # api.

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
