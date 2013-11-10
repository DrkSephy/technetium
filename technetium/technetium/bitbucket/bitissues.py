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


def get_issues_from_subscribed(repo_data, auth_tokens):
    """
    Gets a list back from sending multiple requests to
    get issues from all subscribed repositories.

    Parameters:
    - repo_data: List (Dictionary)
    - auth_tokens: OAuth1

    Returns: List
    """
    repo_issues = []
    for repo in repo_data:
        data = {}
        data['repo_meta']  = repo
        data['raw_issues'] = bitmethods.send_bitbucket_request(
            repo['req_url'], auth_tokens)
        repo_issues.append(data)
    return repo_issues


def parse_issues(repo_issues):
    """
    Parses returned JSON data from the bitbucket API
    response for the technetium issues dashboard.

    Parameters:
    - repo_issues: List of dictionaries of JSON issues

    Returns: List
    """
    # List of repositories, which contains list of parsed issues
    repository_issues = []

    for repo in repo_issues:
        parsed_data = {}
        parsed_data['repo_meta'] = repo['repo_meta']
        parsed_data['issues'] = []
        # Parse general information
        if repo['raw_issues']:
            for issue in repo['raw_issues']['issues']:
                data = {}
                data['title'] = issue['title'].capitalize()
                data['status'] = issue['status'].capitalize()
                data['type'] = issue['metadata']['kind'].capitalize()
                data['priority'] = issue['priority'].capitalize()
                data['created'] = bitmethods.format_timestamp(issue['utc_created_on'])
                parsed_data['issues'].append(data)
        repository_issues.append(parsed_data)
    return repository_issues
