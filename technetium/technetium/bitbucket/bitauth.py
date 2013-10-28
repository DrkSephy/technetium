"""
Module for Bitbucket authentication and authorization.
"""
from social_auth.models import UserSocialAuth


def get_access_secret_tokens(request):
    """
    Gets Access and Secret Tokens out from PSA
    """
    social_user = UserSocialAuth.objects.get(user=request.user)
