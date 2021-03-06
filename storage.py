import pg8000, functools

from config import Config
from tweet import Tweet


def uses_db(f):
    @functools.wraps(f)
    def wrapper(cls, *args, **kwargs):
        cursor = cls._conn.cursor()
        res = f(cls, cursor, *args, **kwargs)
        cursor.close()
        cls._conn.commit()
        return res

    return wrapper


class Storage(object):
    _conn = pg8000.connect(**Config.DB_CONFIG)

    @classmethod
    def generate_tweets(cls):
        cls.put_tweet("First tweet!")
        cls.put_tweet("Second tweet!")
        cls.put_tweet("Cheating tweet!")

    @classmethod
    @uses_db
    def get_tweets(cls, cursor):
        cursor.execute(
            """
            SELECT id, name, tweet FROM tweets
            """
        )
        tweets = [Tweet(*data) for data in cursor.fetchall()]
        return tweets

    @classmethod
    @uses_db
    def get_tweet(cls, cursor, tweet_id):
        cursor.execute(
            """
            SELECT id, name, tweet FROM tweets
            WHERE id=%s
            """,
            (tweet_id,)
        )
        res = cursor.fetchone()
        if res:
            return Tweet(*res)
        else:
            raise TweetNotFoundError("Tweet with id #{} is not found".format(tweet_id))

    @classmethod
    @uses_db
    def put_tweet(cls, cursor, tweet):
        cursor.execute(
            """
            INSERT INTO tweets (name, tweet)
            VALUES ( %s, %s ) RETURNING id, name, tweet
            """,
            (Config.NAME, tweet)
        )
        data = cursor.fetchone()
        new_tweet = Tweet(*data)
        return new_tweet

    @classmethod
    @uses_db
    def delete_tweet(cls, cursor, tweet_id):
        cursor.execute(
            """
        DELETE FROM tweets
        WHERE id=%s
        """,
            (tweet_id,)
        )


class TweetNotFoundError(Exception):
    pass
