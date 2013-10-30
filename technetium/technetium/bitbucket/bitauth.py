"""
Module for Bitbucket authentication and authorization.
"""
from django.conf.settings import BITBUCKET_CONSUMER_KEY, BITBUCKET_CONSUMER_SECRET
from social_auth.models import UserSocialAuth
from requests_oauthlib import OAuth1

def get_social_auth_data(request):
    """
    Gets a dictionary of the following data from social auth:
    1. 'access_token' : {'oauth_token' : String, 'oauth_token_secret' : String}
    2. 'email' : String
    3. 'first_name' : String
    4. 'last_name' : String
    5. 'username' : String

    Returns => Dictionary
    """
    return UserSocialAuth.objects.get(user=request.user).extra_data


def get_auth_tokens(extra_data):
    """
    Returns the authorization tokens required to access
    protected resources from Bitbucket's API. Use this
    function in the 'auth' parameter for requests.

    Parameters:
        - extra_data: Dictionary (from get_social_auth_data)

    Returns: OAuth1 (object)
    """
    tokens = extra_data['access_token']
    resource_owner_key = tokens['oauth_token']
    resource_owner_secret = tokens['oauth_token_secret']
    return OAuth1(BITBUCKET_CONSUMER_KEY,
                  client_secret=BITBUCKET_CONSUMER_SECRET,
                  resource_owner_key=resource_owner_key,
                  resource_owner_secret=resource_owner_secret)
