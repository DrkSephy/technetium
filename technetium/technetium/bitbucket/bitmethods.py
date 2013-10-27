"""
Module for common methods.

Proposed methods:

    - Method for getting a list of all repositories
      belonging to the user.
    - Parsing could probably be refactored into a common method.
"""
#######################
# BITBUCKET CONSTANTS #
#######################
API_BASE_URL = "https://bitbucket.org/api/1.0/repositories/"


def get_repositories():
    """
    Gets all repositories that the user owns/has
    access privledges to.

    Parameters:
    -----------

    Returns:
    --------
    repos: dictionary
        - A dictionary containing a list of all
          repositories owned by the user.
    """

    pass
