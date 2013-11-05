"""
Module for filtering various Bitbucket data.

Handles:
    - Filtering changesets by time/user/date.
    - Filtering issues by type.
    - Filtering issues by priority.
    - Filtering issues by user.
    - Filtering issues by date.
    - Filtering issues by status.
"""
import simplejson as json
import requests

def filter_issues(request, parsed_json):
    """
    Main filter dispatcher
    """

    filtered_json = parsed_json
    for n, v in request.GET.iteritems():
        if n.strip().lower() == 'type':
            filtered_json = filter_issues_by_type(filtered_json, v)
        if n.strip().lower() == 'priority':
            filtered_json = filter_issues_by_priority(filtered_json, v)
        if n.strip().lower() == 'status':
            filtered_json = filter_issues_by_status(filtered_json, v)

    return filtered_json


def filter_issues_by_type(parsed_json, filtered_value):
    """
    Filters issues by type. (Blocker, Status, etc)
    """

    filtered_json = []
    for issue in parsed_json:
        if issue['type'] is not None and issue['type'].strip().lower() == filtered_value.strip().lower():
            filtered_json.append(issue)

    return filtered_json


def filter_issues_by_priority(parsed_json, filtered_value):
    """
    Filters issues based on priority.
    """

    filtered_json = []
    for issue in parsed_json:
        if issue['priority'] is not None and issue['priority'].strip().lower() == filtered_value.strip().lower():
            filtered_json.append(issue)

    return filtered_json


def filter_issues_by_user():
    """
    Filters issues based on users.
    """

    pass


def filter_issues_by_date():
    """
    Filters issues based on date.
    """

    pass

def filter_issues_by_status(parsed_json, filtered_value):
    """
    Filters issues based on status.
    """

    filtered_json = []
    for issue in parsed_json:
        if issue['status'] is not None and issue['status'].strip().lower() == filtered_value.strip().lower():
            filtered_json.append(issue)

    return filtered_json

def filter_changesets_by_date():
    """
    Filters issues based on date/time.
    """

    pass

def filter_changesets_by_user():
    """
    Filters issues based on user.
    """

    pass

