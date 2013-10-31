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


def parse_issues(raw_json):
    """
    Parses returned JSON data from the bitbucket API
    response for the technetium issues dashboard.

    Parameters:
    - raw_json: Dictionary of JSON issues

    Returns: List
    """
    parsed_issues = []

    for issue in raw_json['issues']:
        data = {}

        # Parse general information
        data['title'] = issue['title']
        data['status'] = issue['status']
        data['type'] = issue['metadata']['kind']
        data['priority'] = issue['priority']
        data['created'] = issue['utc_created_on']
        data['issues_url'] = bitmethods.transform_url(issue['resource_uri'])

        # Parse assignee
        data['assignee'] = ''
        data['assignee_avatar'] = ''
        if 'responsible' in issue:
            data['assignee'] = issue['responsible']['display_name']
            data['assignee_avatar'] = issue['responsible']['avatar']

        parsed_issues.append(data)
    return parsed_issues

