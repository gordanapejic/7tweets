import uuid

global_username = "zaba_ljubica"


class Tweet(object):
    def __init__(self, id, name, tweet_body):
        self.id = id
        self.name = name
        self.tweet = tweet_body

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'tweet': self.tweet
        }

    @classmethod
    def from_dict(cls, data):
        return Tweet(**data)
