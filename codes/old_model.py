import time
import random
from peewee import *
import datetime


class CrawlerAccount(BaseModel):
    username = CharField(unique=True)
    email  = CharField(unique=True)
    password = CharField()
    full_name = CharField(null=True)
    latest_use_time = DateTimeField(null=True)


def get_next_crawler_account(i):
    minutes = random.randint(1, 5)
    while True:
        hour_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=0)# datetime.time.hour() #- datetime.timedelta(hour=1)
        account = CrawlerAccount.get_or_none(CrawlerAccount.latest_use_time <=  hour_ago )
        if account != None:
            account.latest_use_time = datetime.datetime.now()
            print("temp is:", account)
            account.save()
            return account.username, account.password
        
        time.sleep(10)

def add_relationship(follower, following):
    Relationship.create(from_user= follower, to_user=following)

def add_user_followers(user_instagram_id, followers_jsons):
    # relations = [Relationship(from_user=int(follower["id"]), to_user=user_instagram_id) for follower in followers_jsons]
    relations = [(int(follower['id']),int(user_instagram_id)) for follower in followers_jsons]
    new_users = [{'id':f['id'],'username':f['username'], 'full_name': f['full_name'], 'profile_picture':f['profile_picture']} for f in followers_jsons]
    # Relationship.insert_many(new_users).execute()
    # Relationship.insert_many(relations).on_conflict_replace().execute()
    # Relationship.insert_many(relations).on_conflict_replace().execute()
    User.insert_many(new_users).on_conflict_ignore().execute()
    Relationship.insert_many(relations, fields=[Relationship.from_user, Relationship.to_user]).on_conflict_ignore().execute()
    
##
def add_user_posts(user_id, posts_jsons):
    for ps in posts_jsons:
        Post.create_from_json(ps)
    



redis_client = redis.Redis(host='localhost', port=6379, db=0)
REDIS_KEY_USERS = 'key_users'

def renew_users():
    users = User.select()#.execute()
    for u in users:
        print("usid:", u.id)
        redis_client.rpush(REDIS_KEY_USERS, u.id)
def get_next_user():
    print( "len0:",redis_client.llen(REDIS_KEY_USERS))
    if redis_client.llen(REDIS_KEY_USERS) < 1:
        renew_users()
    print( "len1:",redis_client.llen(REDIS_KEY_USERS))
    return str(int(redis_client.lpop(REDIS_KEY_USERS)))

