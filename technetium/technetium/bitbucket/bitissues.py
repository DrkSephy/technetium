"""
Module for Bitbucket issues aggregation.

Bitbucket API requests start at the following layout:

https://bitbucket.org/api/1.0/repositories/{accountname}/{repo_slug}/{endpoint}

    - {accountname} : The Bitbucket User name
    - {repo_slug} : The repository name
    - {endpoint} : The resource to request

The calls also take the following extra query parameters:

    - start: The hash value which the query starts from. The
             default start point is the most recent entry to
             the earliest.

    - limit: Integer value which represents the number of changesets
             to return.
"""
import simplejson as json
import requests
import bitmethods


def get_issues(user, repo, auth_tokens, limit):
    """
    Obtains a JSON dictionary from issues endpoint.

    Parameters:
    - user: User (Django)
    - repo: String
    - auth_tokens: OAuth1
    - limit: Integer

    Returns: Dictionary
    """
    req_url = bitmethods.make_req_url(user, repo, 'issues', limit)
    return bitmethods.send_bitbucket_request(req_url, auth_tokens)


def parse_issues(issues):
    """
    Parses returned JSON data from the bitbucket API
    response for the technetium issues dashboard.

    Parameters:
    - issues: Dictionary of JSON issues

    Returns: List
    """

    x = issues['issues']

    # List of non-nested keys to parse out
    keys = ['status', 'title', 'priority']

    # list of nested keys to parse out
    nested_keys = ['kind', 'component']

    # Empty list of new dictionaries
    issue = []

    # x is the array of issues
    # a represents a dictionary inside x, which is an issue
    # there are multiple a's
    for a in x:
        new_list = {}
        for k,v in a.iteritems():
            if k in keys:

        # Create a new list of dictionaries for each issue 
        # containing the key,value pairs that we want
                new_list[k] = v
            # Iterate through keys which have dictionaries as values
            # This iteration goes through nested dictionaries and looks
            # up keys from vreqs
            if isinstance(v, dict):
                for key, value in v.iteritems():
                    if key in nested_keys:
                        new_list[key] = value
        issue.append(new_list)
    
    return issue

    