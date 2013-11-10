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
import technetium.bitbucket.bitmethods as bitmethods
import technetium.bitbucket.bitfilter as bitfilter


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


def get_issues_from_subscribed(req_urls, auth_tokens):
    """
    Gets a list back from sending multiple requests to
    get issues from all subscribed repositories.

    Parameters:
    - req_urls: List (String: URLs)
    - auth_tokens: OAuth1

    Returns: List (of Dictionaries)
    """
    repo_issues = []
    for url in req_urls:
        repo_issues.append(bitmethods.send_bitbucket_request(url, auth_tokens))
    return repo_issues


def parse_issues(name_val_dict, repo_json):
    """
    Parses returned JSON data from the bitbucket API
    response for the technetium issues dashboard.

    Parameters:
    - repo_json: List of dictionaries of JSON issues

    Returns: List
    """
    parsed_issues = []
    assignee_list = []

    for repo in repo_json:
        for issue in repo['issues']:
            data = {}

            # Parse general information
            data['title'] = issue['title'].capitalize()
            data['status'] = issue['status'].capitalize()
            data['type'] = issue['metadata']['kind'].capitalize()
            data['priority'] = issue['priority'].capitalize()
            data['created'] = bitmethods.format_timestamp(issue['utc_created_on'])
            data['issues_url'] = '#'

            # Parse assignee
            data['assignee'] = ''
            data['assignee_avatar'] = ''
            if 'responsible' in issue:
                data['assignee'] = issue['responsible']['display_name']
                data['assignee_avatar'] = issue['responsible']['avatar']

            parsed_issues.append(data)
            if not data['assignee']:
                if data['assignee'].strip() not in assignee_list:
                    assignee_list.append(data['assignee'].strip())

        # Filter issues based on query parameters
        parsed_issues = bitfilter.filter_issues(name_val_dict, parsed_issues)

    return parsed_issues, assignee_list

