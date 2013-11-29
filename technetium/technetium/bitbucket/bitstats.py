"""
Module to get statistics of repositories
"""
import bitmethods
import bitchangesets


def tally_changesets(data):
    """
    Counts the number of commits for each developer in a repository.

    Parameters:
        data: Dictionary
            - A dictionary containing the commits to be tallied.

    Returns:
        tally: Dictionary
            - A dictionary containing the sums of all commits in the
              repository.

    Example:
        { 'David Leonard' : {'changesets' : 9}, ...}
    """
    tally = {}
    for changeset in data:
        author = changeset['parsed_author']
        if author not in tally:
            tally[author] = {'changesets' : 1}
        else:
            tally[author]['changesets'] += 1
    return tally


def tally_assigned_issues(data):
    """
    Gets the number of issues that each user has been assigned.

    Parameters:
        data: Dictionary
            - A dictionary containing all assigned issues to be tallied.

    Returns:
        tally: Dictionary
            - A dictionary containing the tally of all assigned issues for
              all users in a repository.

    Example: Returns {accountname: 8, DrkSephy: 5}, which is a
    dictionary of the number of issues the above user resolved.
    """
    pass


def tally_issue_comments(data):
    """
    Gets the number of comments that each user has made.
    """
    pass


def tally_opened_issues(data):
    """
    Gets the number of issues each user has opened.

    Notes: Even though issues are usually opened by the scrum master,
    we still need this to grade them.

    Returns:
        opened_issues: Dictionary
            - A dictionary containing number of issues that each
              user in a given repository has opened.
    """
    pass


def list_users(data):
    """
    Returns a list of all developers in a repository.
    Useful for generating D3 graphs.

    Paramters:
        data: Dictionary
            - A dictionary containing users [keys] to be turned into a list.

    Returns:
        devs: List
            - A list containing the developers of a given repository.
    """
    devs = []
    for key, value in data.iteritems():
        devs.append(key)
    return devs


def list_data(data, key_value='changesets'):
    """
    Returns a list of data in order of developers.
    Useful for D3 graphs. You can use this to list
    commit data as well as issues.

    Paramters:
        data: Dictionary
            - A dictionary containing commits [keys] to be turned into a list.

    Returns:
        commits: List
            - A list containing the number of commits for each user
              of a given repository.
    """
    commits = []
    for key, value in data.iteritems():
        commits.append(value[key_value])
    return commits


def list_timestamp_and_user(changesets):
    """
    Will be modified in the future for commits linegraph

    Returns a tuple of list containing:
    (1) timestamps
    (2) usernames
    """
    timestamps = []
    usernames  = []
    for commit in changesets:
        timestamps.append(commit['timestamp'])
        usernames.append(commit['parsed_author'])
    return (timestamps, usernames)
