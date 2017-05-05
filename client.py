import requests
import json

url = "http://127.0.0.1:5000/tweets"
r = requests.get(url+"/load")
print(r.text)

r = requests.post(url, json=json.dumps({'tweet': 'Hello from the app!'}))
print(r.text)

r = requests.post(
    url=url,
    json=json.dumps({'tweet': 'Raven!'})
)
print(r.text)

r = requests.post(
    url=url,
    json=json.dumps({'tweet': 'The most beautiful tweer!'})
)
print(r.text)

r = requests.get(url)
print(r.text)


r = requests.post(
    url=url,
    json=json.dumps({'tweet': 'The fourth, the luck!'})
)
print(r.text)

r = requests.get(url)
print(r.text)

tweet_id = r.json()[0]["id"]
r = requests.get("{}/{}".format(url, tweet_id))
print("> get tweet #{}:\n{}".format(tweet_id, r.text))


r = requests.delete("{}/{}".format(url, tweet_id))
print(r.text)
