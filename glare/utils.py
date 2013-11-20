import requests
from social.apps.django_app.utils import load_strategy


def qjson(user, path):
    u = user.social_auth.get()
    token = u.tokens
    params = {'access_token': token}
    return requests.get(path, params=params).json()


def rtoken(user):
    s = load_strategy(backend='google-oauth2')
    u.refresh_token(s)
