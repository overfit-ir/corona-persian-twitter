from peewee import *
import datetime
DATABASE = 'tweepee.db'
database = PostgresqlDatabase('socialyticsDB')
                           #SqliteDatabase(DATABASE)

#pipe = redis_client.pipeline()
class BaseModel(Model):
    class Meta:
        database = database
    # @classmethod
    # def bulk_create_from_json(cls):


class User(BaseModel):
    id = BigIntegerField( primary_key = True)
    username = CharField()#unique=True)
    full_name = CharField(null=True)
    is_verified = BooleanField(default=False)
    profile_picture = CharField(null=True)
    following_count = IntegerField()
    follower_count = IntegerField()
    is_condidate = BooleanField()

    # def set_and_check_language(language):
    #     if language = fa

class Tweet(BaseModel):
    id = BigIntegerField(unique=True)
    #id = AutoField(unique=True)
    # tweeter_id = CharField(unique=True)
    user = ForeignKeyField(User,  backref="tweets") #may be user and owner are diferent
    replies_count = IntegerField()
    likes_count = IntegerField()
    retweets_count = IntegerField()
    qoutes_count = IntegerField()
    text = TextField(null=True) #with hashtag
    hashtags = [list of TextField]
    media_src = CharField(max_length=511, default= None)
    datetime = TimestampField()
    # link = CharField(max_length=511) 
    # media_type = CharField()
    def getlink():
        pass



    @classmethod
    def create_from_json(cls, post_json):
        print("pj is", post_json)
        pj = post_json.get('node')
        caption = pj.get('caption', None)
        if caption == None:
            caption_text = None
            caption_id = None
        else:
            caption_text = caption['text']
            caption_id = caption['id']
        return Post.create(instagram_id=pj['id'],user=pj['user']['id'],shortcode=pj['shortcode'], comments_count=pj['comments']['count'],
        likes_count=pj['likes']['count'],taken_at_timestamp=int(pj['taken_at_timestamp']),
        instagram_created_time=int(pj['created_time']),caption=caption_text, caption_id=caption_id,
        comment_disabled=pj['comments_disabled'],location=pj['location'],link=pj['link'],
        media_src=pj['display_url'],media_type_name=pj['__typename'],
        media_type=pj['type'],media_width=pj['dimensions']['width'], media_height=pj['dimensions']['height'])

    
class Reply(Tweet):
    parent_tweet = ForeignKeyField(Tweet, backref='replies')
    is_Qoute = BooleanField(default=False)


# class Reply(BaseModel):
#     text = TextField()
#     user = ForeignKeyField(User, backref='replies')
#     tweet = ForeignKeyField(Tweet, backref='replies')

class Like(BaseModel):
    liker = ForeignKeyField(User, backref='likes')
    tweet = ForeignKeyField(Tweet, backref='likes')
    # likie_user = Fo


class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='followings',null=True)
    to_user = ForeignKeyField(User, backref='followers', null=True)
    # from_user = BigIntegerField()
    # to_user = ForeignKeyField(User, backref='followers', null=True)
    # latest_update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        # `indexes` is a tuple of 2-tuples, where the 2-tuples are
        # a tuple of column names to index and a boolean indicating
        # whether the index is unique or not.
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('from_user', 'to_user'), True),
        )
database.create_tables([User, Tweet, Like, Relationship])
# def add_user(user_json, is_farsi):


