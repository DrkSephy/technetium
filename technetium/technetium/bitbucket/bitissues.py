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


def parse_all_issues(repo_issues):
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
        parsed_data['issues'] = parse_issues(repo['raw_issues']['issues'])
        repository_issues.append(parsed_data)
    return repository_issues


def parse_issues(issues):
    """
    Parse issues from Dictionary

    Returns: List
    """
    parsed_issues = []
    for issue in issues:
        data = {}

        # Parse issue information
        data['title'] = issue['title'].capitalize()
        data['status'] = issue['status'].capitalize()
        data['type'] = issue['metadata']['kind'].capitalize()
        data['priority'] = issue['priority'].capitalize()
        data['created'] = bitmethods.format_timestamp(issue['utc_created_on'])
        data['issues_url'] = "#"

        # Parse assignee
        data['assignee'] = ''
        data['assignee_avatar'] = ''
        if 'responsible' in issue:
            data['assignee'] = issue['responsible']['display_name']
            data['assignee_avatar'] = issue['responsible']['avatar']
        parsed_issues.append(data)
    return parsed_issues
