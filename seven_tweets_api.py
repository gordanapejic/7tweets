import json

from flask import Blueprint, request, jsonify

from storage import Storage, TweetNotFoundError

tweets_api = Blueprint('tweets', __name__)


def json_response(message="OK", status=200):
    return jsonify({"status": status, "message": message}), status


@tweets_api.route("/tweets", methods=['GET'])
def get_tweets():
    return json_response([tweet.to_dict() for tweet in Storage.get_tweets()], 200)


@tweets_api.route("/tweets/<tweet_id>", methods=['GET'])
def get_tweet(tweet_id):
    try:
        tweet = Storage.get_tweet(tweet_id)
        return json_response(tweet.to_dict(), 200)
    except TweetNotFoundError as err:
        return json_response(str(err), 404)


@tweets_api.route("/tweets", methods=['POST'])
def post_tweet():
    Storage.put_tweet(json.loads(request.get_json())["tweet"])
    return json_response()


@tweets_api.route("/tweets/<tweet_id>", methods=['DELETE'])
def delete_tweet(tweet_id):
    Storage.delete_tweet(tweet_id)
    return json_response()

