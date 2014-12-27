import oauth2 as oauth

from secret import linkedin


def get_client():
    # Keys and secrets from app registration
    consumer_key    =   linkedin['consumer_key']
    consumer_secret =   linkedin['consumer_secret']
    user_token      =   linkedin['user_token']
    user_secret     =   linkedin['user_secret']

    # Consumer object
    consumer = oauth.Consumer(consumer_key, consumer_secret)

    # Client object
    client = oauth.Client(consumer)

    # Access token object using developer token and secret
    access_token = oauth.Token(key=user_token, secret=user_secret)

    return oauth.Client(consumer, access_token)


def get_full_profile():
    client = get_client()

    fields = ['positions', 'skills', 'honors-awards', 'courses']
    st = ",".join(fields)

    url = "https://api.linkedin.com/v1/people/~:(" + st + ")?format=json"

    # Call LinkedIn to retrieve profile
    resp, content = client.request(url, "GET")

    return content, resp.status
