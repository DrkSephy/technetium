"""
Module for Bitbucket authentication and authorization.

Read up on OAuth1 Workflow:
http://requests-oauthlib.readthedocs.org/en/latest/oauth1_workflow.html

"""
from django.conf import settings
from social_auth.models import UserSocialAuth
from requests_oauthlib import OAuth1

def get_social_auth_data(user_id):
    """
    Gets a dictionary of the following data from social auth:
    1. 'access_token' : {'oauth_token' : String, 'oauth_token_secret' : String}
    2. 'email' : String
    3. 'first_name' : String
    4. 'last_name' : String
    5. 'username' : String

    Parameters:
    - user_id: User (Django object)

    Returns => Dictionary
    """
    return UserSocialAuth.objects.get(user=user_id).extra_data


def get_auth_tokens(extra_data):
    """
    Returns the authorization tokens required to access
    protected resources from Bitbucket's API. Use this
    function as the 'auth' parameter for requests.

    Note: The client and client_secret come from the settings.

    Parameters:
        - extra_data: Dictionary (from get_social_auth_data())

    Returns: OAuth1 (object)
    """
    tokens = extra_data['access_token']
    resource_owner_key = tokens['oauth_token']
    resource_owner_secret = tokens['oauth_token_secret']
    return OAuth1(settings.BITBUCKET_CONSUMER_KEY,
                  client_secret=settings.BITBUCKET_CONSUMER_SECRET,
                  resource_owner_key=resource_owner_key,
                  resource_owner_secret=resource_owner_secret)
