from flask import Flask
from seven_tweets_api import tweets_api
from storage import Storage

app = Flask(__name__)
app.register_blueprint(tweets_api)


if __name__ == "__main__":
    Storage.generate_tweets()
    app.run(host="0.0.0.0", port=5000, debug=True)
