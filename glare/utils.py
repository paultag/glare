from social.apps.django_app.utils import load_strategy
from requests.exceptions import HTTPError
import requests
import json


def request(u, *args, **kwargs):
    """
    Wrapper for request.request, but refresh the token if we can't nom.
    """
    try:
        req = requests.request(*args, **kwargs)
    except HTTPError:
        s = load_strategy(backend='google-oauth2')
        u.refresh_token(s)
        req = requests.request(*args, **kwargs)
    req.raise_for_status()
    return req.json()


def GET(user, url, params=None):
    if params is None:
        params = {}

    u = user.social_auth.get()
    params['access_token'] = u.tokens
    return request(u, "GET", url, params=params)


def POST(user, url, headers=None, data=None):
    if headers is None:
        headers = {}

    data['menuItems'] = [
        {
            "id": 'delete',
            "action": "Delete",
            "values": [
                {
                    "displayName": "Delete",
                }
            ],
            "removeWhenSelected": True,
            "payload": "Delete",
        }
    ]

    data = json.dumps(data)
    u = user.social_auth.get()
    headers['Authorization'] = "Bearer {token}".format(token=u.tokens)
    headers['Content-Type'] = "application/json"
    return request(u, "POST", url, headers=headers, data=data)
