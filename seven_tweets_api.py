import json

from flask import Blueprint, request, jsonify

from storage import Storage

tweets_api = Blueprint('tweets', __name__)


@tweets_api.route("/tweets", methods=['GET'])
def get_tweets():
    return jsonify([tweet.to_dict() for tweet in Storage.get_tweets()]), 200


# Ne radi
@tweets_api.route("/tweets/<tweet_id>", methods=['GET'])
def get_tweet(tweet_id):
    tweet = Storage.get_tweet(tweet_id)
    return jsonify(tweet.to_dict()), 200
  #      if tweet else "Not found", 404


@tweets_api.route("/tweets", methods=['POST'])
def post_tweet():
    return jsonify(Storage.put_tweet(json.loads(request.get_json())["tweet"]))


@tweets_api.route("/tweets/<tweet_id>", methods=['DELETE'])
def delete_tweet(tweet_id):
    result = Storage.delete_tweet(tweet_id)
    return jsonify(result), 200
