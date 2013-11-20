from social.apps.django_app.utils import load_strategy
import json


def qjson(user, path):
    u = user.social_auth.get()
    s = load_strategy(backend='google-oauth2')
    u.refresh_token(s)
