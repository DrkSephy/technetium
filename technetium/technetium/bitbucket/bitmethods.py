"""
Module for common bitbucket methods.

Proposed methods:
    - Parsing could probably be refactored into a common method.
"""
import simplejson as json
from datetime import datetime
import requests

#######################
# BITBUCKET CONSTANTS #
#######################
API_BASE_URL = "https://bitbucket.org/api/1.0/repositories/"
BITBUCKET_BASE_URL = "https://bitbucket.org/"


def make_req_url(user, repo, endpoint, limit=None, start=None):
    """
    Constructs a URL for bitbucket API request.

    Parameters:
    - user: String
    - repo: String
    - endpoint: String
    - limit: Integer (Max 50)
    - start: Integer

    Returns: String

    Example:
    Params: (user='technetiumccny', repo='technetium', endpoint='issues')
    Output: 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'
    """
    url = "%s%s/%s/%s" % (API_BASE_URL, user, repo, endpoint)

    # Set limit is given and is above 50, set limit to 50
    if limit and limit > 50:
        limit = 50

    # Handle extra queries
    if limit and start:
        url += "?limit=%d&start=%d" % (limit, start)
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


def format_timestamp(timestamp):
    """
    Formats string timestamp into readable timestamp.
    """
    try:
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S+00:00')
        return datetime.strftime(date, '%m-%d-%Y')
    except ValueError:
        return ''
