"""
This module contains methods responsible for handling OAuth tokens needed for
interacting with the Bitbucket API. As required by Bitbucket, OAuth1 is required
to make API calls to any private repository.
"""
from django.conf import settings
from social_auth.models import UserSocialAuth
from requests_oauthlib import OAuth1


def get_auth_tokens(user_id):
    """
    Returns the authorization tokens required to access
    protected resources from Bitbucket's API. Use this
    function as the 'auth' parameter for requests.

    Note: The client and client_secret come from the settings.

    Parameters:
        extra_data: Dictionary (from get_social_auth_data())

    Returns:
        OAuth1 (object)
    """
    extra_data = UserSocialAuth.objects.get(user=user_id).extra_data
    tokens = extra_data['access_token']
    resource_owner_key = tokens['oauth_token']
    resource_owner_secret = tokens['oauth_token_secret']
    return OAuth1(settings.BITBUCKET_CONSUMER_KEY,
                  client_secret=settings.BITBUCKET_CONSUMER_SECRET,
                  resource_owner_key=resource_owner_key,
                  resource_owner_secret=resource_owner_secret)
