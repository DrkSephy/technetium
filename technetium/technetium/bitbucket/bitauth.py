"""
Module for Bitbucket authentication and authorization.
"""
from social_auth.models import UserSocialAuth


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

