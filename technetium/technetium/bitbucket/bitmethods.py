"""
Module for common methods.

Proposed methods:

    - Method for getting a list of all repositories
      belonging to the user.
    - Parsing could probably be refactored into a common method.
"""
import simplejson as json
import requests

#######################
# BITBUCKET CONSTANTS #
#######################
API_BASE_URL = "https://bitbucket.org/api/1.0/repositories/"


def make_req_url(user, repo, endpoint, limit=None, start=None):
    """
    Constructs a URL for bitbucket API request.

    Parameters:
    - user: String
    - repo: String
    - endpoint: String
    - limit: Integer
    - start: Integer

    Returns: String

    Example:
    Params: (user='technetiumccny', repo='technetium', endpoint='issues')
    Output: 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'
    """
    url = "%s%s/%s/%s" % (API_BASE_URL, user, repo, endpoint)

    # Handle extra queries
    if limit and start:
        url += "?limit=%d&%d" % (limit, start)
    elif limit:
        url += "?limit=%d" % limit
    elif start:
        url += "?start=%d" % start
    return url


def send_bitbucket_request(req_url, auth_tokens):
    """
    Obtains a JSON dictionary from bitbucket API endpoint.

    Parameters:
    - req_url: String (URL)
    - auth_tokens: OAuth1 (Object)

    Returns => Dictionary
    """
    # Success status 200, return JSON
    req = requests.get(req_url, auth=auth_tokens)
    if req.status_code == 200:
        return json.loads(req.content)
    return {}


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


def unicode_to_str(data):
    """
    Recursively convert a collection containing unicode strings to strings.
    Call this method on the JSON returned from Bitbucketself.

    Returns: String
    """
    if isinstance(data, str):
        return data
    elif isinstance(data, unicode):
        return str(data)
    else:
        return data

