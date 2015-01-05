from flask import json
import oauth2 as oauth
from secret_credentials import slinkedin


def get_client():
    # Keys and secrets from app registration
    consumer_key    = slinkedin['consumer_key']
    consumer_secret = slinkedin['consumer_secret']
    user_token      = slinkedin['user_token']
    user_secret     = slinkedin['user_secret']

    # Consumer object
    consumer = oauth.Consumer(consumer_key, consumer_secret)

    # Client object
    client = oauth.Client(consumer)

    # Access token object using developer token and secret
    access_token = oauth.Token(key=user_token, secret=user_secret)

    return oauth.Client(consumer, access_token)


def get_full_profile():
    client = get_client()

    # Select fields from:
    # https://developer.linkedin.com/documents/profile-fields
    fields = [  'first-name', 'last-name', 'headline', 'location',
                'positions', 'skills', 'honors-awards', 'courses'  ]

    st = ",".join(fields)
    url = "https://api.linkedin.com/v1/people/~:(" + st + ")?format=json"

    # Call LinkedIn to retrieve profile
    resp, content = client.request(url, "GET")
    js = json.loads(content) # Convert to dictionary

    if resp.status == 200:
        return { "content" : js }, resp.status

    else: # Return informative error message as dictionary
        return { "error message" : js["message"] }, resp.status
