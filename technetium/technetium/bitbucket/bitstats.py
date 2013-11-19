"""
Module for computing statistics for Bitbucket.
"""

import requests
import simplejson as json

def tally_changesets(data):
    """
    Counts the number of commits for each developer in a repository.

    Parameters:
    -----------
    data: dictionary

    Returns:
    --------
    tally: dictionary
    """
    #data = [{'author': 'Kevin Chan'}, {'author': 'Kevin Chan'}]
    # Dictionary to store commit counts
    tally = {}
    # Iterate over all dictionaries in our list
    if data != None:
        for i in data:
            for k,v in i.iteritems():
                # If author is in dictionary, +=1.
                # Otherwise, add the author to the dictionary
                # and start his counter to be 1.
                if v in tally:
                    tally[v] += 1
                else:
                    tally[v] = 1

        # Return a dictionary of the tally.
        # Example: {DrkSephy: 9, Jorge Yau: 15}
        return tally


def tally_assigned_issues(data):
    """
    Gets the number of issues that each user has been assigned.

    Parameters:
    - data: dictionary

    Returns: Dictionary

    Example: Returns {accountname: 8, DrkSephy: 5}, which is a
    dictionary of the number of issues the above user resolved.
    """
    pass



def tally_issue_comments(data):
    """
    Gets the number of comments that each user has made.

    Notes: Needs to check each issue endpoint and get a tally
    of all comments made.

    Returns:
    --------
    issue_comments: dictionary containing number of comments for
                    each user.
    """

    pass

def tally_opened_issues(data):
    """
    Gets the number of issues each user has opened.

    Notes: Even though issues are usually opened by the scrum master,
    we still need this to grade them.

    Returns:
    --------
    opened_issues: dictionary containing number of issues that each
                   user has opened.
    """

    pass


def list_users(data):
    """
    Returns a list of all developers in a repository.
    Useful for plugging directly into the Pie Chart.
    """

    devs = []
    for k,v in data.iteritems():
        devs.append(k)
    return devs

def list_commits(data):
    """
    Returns a list of commits in order of developers.
    Useful for graphs.
    """

    commits = []
    for k,v in data.iteritems():
        commits.append(v)
    return commits
