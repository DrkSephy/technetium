"""
Module for interacting with Bitbucket Issue data. This module contains
methods for bundling request URLs to Bitbucket, for parsing JSON data
relating to Issues, and auxillary methods for preparing the data for use
inside of Technetium's Subscription Manager.
"""
from django.template.loader import render_to_string
import bitmethods


###########
# REPORTS #
###########
def get_issues_urls(user, repo, endpoint, end, limit=50):
    """
    Makes a list of api urls based on iterating through limit.
    Uses make_req_url() as a helper function.

    Returns:
        content: List
    """
    req_urls = []
    count = 0
    while count < end:
        new_url = bitmethods.make_req_url(user, repo, endpoint, limit, count)
        req_urls.append(new_url)
        count += limit
    return req_urls


def parse_all_issues(repo_issues):
    """
    Parses returned JSON data from the bitbucket API
    response for the technetium issues dashboard.

    Parameters:
        repo_issues: List (Dictionaries of JSON issues)

    Returns:
        List
    """
    # List of repositories, which contains list of parsed issues
    issues_list = []
    for repo in repo_issues:
        if 'issues' in repo:
            issues_list.append(parse_issues(repo['issues']))
        else:
            issues_list.append([])
    return issues_list


def parse_issues(issues):
    """
    Parse issues from Dictionary

    Parameters:
        issues: List

    Returns:
        List
    """
    parsed_issues = []
    # No issues in repository
    if not issues:
        return parsed_issues

    # Parse issue information
    for issue in issues:
        data = {}
        data['title'] = issue['title'].capitalize()
        data['status'] = issue['status'].capitalize()
        data['type'] = issue['metadata']['kind'].capitalize()
        data['priority'] = issue['priority'].capitalize()
        data['date'] = bitmethods.format_timestamp(issue['utc_last_updated'])
        data['issues_url'] = "#"

        # Parse assignee
        data['assignee'] = ''
        data['assignee_avatar'] = ''
        if 'responsible' in issue:
            data['assignee'] = issue['responsible']['display_name']
            data['assignee_avatar'] = issue['responsible']['avatar']
        parsed_issues.append(data)
    return parsed_issues


def attach_meta(subscription, repo_issues):
    """
    Creates a list of Dictionaries that attaches meta
    infomation to each list of issues.

    Returns:
        List
    """
    repo_list = []
    # Attach meta data for each repo's issues
    for i in xrange(len(subscription)):
        data = {'issues' : repo_issues[i]}
        repo = subscription[i]
        meta = {
                'repo_name' : repo.repository,
                'repo_owner' : repo.owner,
                'repo_slug' : repo.slug_url,
                }
        data['repo_meta']  = meta
        repo_list.append(data)
    return repo_list


def add_html_issue_rows(parsed_data):
    """
    Takes parsed issues and returns HTML to attach to rows.
    There has to be a better way of doing this.

    Parameters:
        parsed_data: Dictionary

    Returns:
        String
    """
    html = 'includes/issues/issues-list.html'
    return render_to_string(html, {'repo' : {'issues' : parsed_data}})
