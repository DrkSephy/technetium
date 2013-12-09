"""
Module containing functions for filtering issues
"""
import simplejson as json


def filter_issues(name_val_dict, parsed_json):
    """
    Main filter dispatcher for issues.
    """

    filtered_json = parsed_json
    for name, value in name_val_dict.iteritems():
        n_strip = name.strip().lower()
        v_strip = value.strip().lower()
        if n_strip == 'type':
            filtered_json = filter_issues_by_type(filtered_json, v_strip)
        if n_strip == 'priority':
            filtered_json = filter_issues_by_priority(filtered_json, v_strip)
        if n_strip == 'status':
            filtered_json = filter_issues_by_status(filtered_json, v_strip)
        if n_strip == 'assignee':
            filtered_json = filter_issues_by_user(filtered_json, v_strip)

    return filtered_json


def filter_issues_by_type(parsed_json, filtered_value):
    """
    Filters issues by type.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'type' in issue:
            if issue['type'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_priority(parsed_json, filtered_value):
    """
    Filters issues based on priority.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'priority' in issue:
            if issue['priority'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_user(parsed_json, filtered_value):
    """
    Filters issues based on users.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'assignee' in issue:
            j_assignee = issue['assignee']
            if issue['assignee'].strip().lower()==filtered_value:
                filtered_json.append(issue)
            elif filtered_value == 'unassigned' and j_assignee == '':
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_status(parsed_json, filtered_value):
    """
    Filters issues based on status.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'status' in issue:
            if issue['status'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json

