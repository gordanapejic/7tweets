import json, uuid

global_username = "zaba_ljubica"


class Tweet(object):
    def __init__(self, tweet_body):
        self.id = str(uuid.uuid4())
        self.name = global_username
        self.tweet = tweet_body

    def to_dict(self):
        return self.__dict__


class Storage(object):
    _tweets = {}
    _counter = 0

    @classmethod
    def generate_tweets(cls):
        cls.put_tweet("First tweet!")
        cls.put_tweet("Second tweet!")
        cls.put_tweet("Cheating tweet!")

    @classmethod
    def get_tweets(cls):
        return cls._tweets.values()

    @classmethod
    def get_tweet(cls, tweet_id):
        if cls._tweets.get(tweet_id, None):
            return cls._tweets[tweet_id]
        else:
            return None

    @classmethod
    def put_tweet(cls, tweet):
        new_tweet = Tweet(tweet)
        cls._tweets[new_tweet.id] = new_tweet

    @classmethod
    def delete_tweet(cls, tweet_id):
        if cls._tweets.get(tweet_id, None):
            del cls._tweets[tweet_id]
            return "OK"
        else:
            return "No tweet with id #{}".format(tweet_id)