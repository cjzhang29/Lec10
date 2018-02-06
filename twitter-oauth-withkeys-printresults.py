from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
resp = oauth.get(protected_url, params=params).json()
status = resp["statuses"]
for s in status:
    user = s["user"]
    print(user["name"])
    print(s["text"])
    print("----------")
#with open('tweet.json', 'w') as outfile:
#    json.dump(resp, outfile, sort_keys=True, indent=4)
