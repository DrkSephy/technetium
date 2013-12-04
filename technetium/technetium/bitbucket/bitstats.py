"""
Module containing methods for generating Technetium's reports. These 
methods include the ability to create tallies of both changeset and 
issue data for each user in a given repository. 
"""
import bitmethods


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


def parse_issues_for_tallying(req_urls, auth_tokens):
    """
    Grabs all issues in a repository with async requests.
    Purpose is to parse issues open, assigned, and resolved.
    """
    parsed_issues = []
    if req_urls:
        raw_issues = bitmethods.send_async_bitbucket_requests(req_urls, auth_tokens)
        for issues_list in raw_issues:
            for issue in issues_list['issues']:
                data = {}
                data['status']  = issue['status']
                data['issue_id']  = issue['local_id']
                data['opened_by'] = issue['reported_by']['display_name']
                data['timestamp'] = issue['utc_last_updated']
                data['assigned']  = None
                if 'responsible' in issue:
                    data['assigned'] = issue['responsible']['display_name']
                parsed_issues.append(data)
    return parsed_issues


def tally_issues(issues):
    """
    Gets the number of issues that each user has been assigned.

    Parameters:
        data: List
            - A List containing all parsed issues to be tallied.

    Returns:
        tally: Dictionary
            - A dictionary containing the tally of all assigned issues for
              all users in a repository.
    """
    tally = {}

    for issue in issues:
        # Tally up who opened the issue
        reporter = issue['opened_by']
        if reporter not in tally:
            tally[reporter] = new_issues_tally()
        tally[reporter]['issues_opened'] += 1

        # Tally up who was assigned the issue
        assigned = issue['assigned']
        if assigned:
            if assigned not in tally:
                tally[assigned] = new_issues_tally()
            tally[assigned]['issues_assigned'] += 1

            # Tally up issues completed if issue was completed
            if issue['status'] == 'resolved':
                tally[assigned]['issues_completed'] += 1
    return tally


def new_issues_tally():
    """
    Helper function for tally issues
    """
    return {'issues_opened' : 0,
            'issues_assigned' : 0,
            'issues_completed' : 0 }


def combine_tallies(changesets_tallied, issues_tallied):
    """
    Returns a dictionary where tallies for issues and changesets
    are merged into a single dictionary.

    Parameters:
        changesets_tallied: Dictionary
        issues_tallied: Dictionary

    Returns:
        Dictionary
    """
    # Check in changesets if they made an issue
    for user in changesets_tallied:
        if user in issues_tallied:
            for tally in issues_tallied[user]:
                changesets_tallied[user][tally] = issues_tallied[user][tally]
            del issues_tallied[user]
        else:
            changesets_tallied[user]['issues_opened'] = 0
            changesets_tallied[user]['issues_assigned'] = 0
            changesets_tallied[user]['issues_completed'] = 0

    # Handle case if user has issues but not commits
    for user in issues_tallied:
        changesets_tallied[user] = issues_tallied[user]
        changesets_tallied[user]['changesets'] = 0
    return changesets_tallied


def tally_issue_comments(data):
    """
    Gets the number of comments that each user has made.
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

def list_data_issues(data, key_value='issues_completed'):
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
    issues_completed = []
    for key, value in data.iteritems():
        issues_completed.append(value[key_value])
    return issues_completed


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
