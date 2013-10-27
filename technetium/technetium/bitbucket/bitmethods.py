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

def make_req_url(user, repo, endpoint, limit=None):
    """
    Constructs a URL for bitbucket API request.

    Parameters:
    - user: String
    - repo: String
    - endpoint: String
    - limit: Integer

    Returns: String

    Example:
    Params: (user='technetiumccny', repo='technetium', endpoint='issues')
    Output: 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'
    """
    url = "%s%s/%s/%s" % (API_BASE_URL, user, repo, endpoint)
    if limit:
        url += "?limit=%d" % limit
    return url


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
