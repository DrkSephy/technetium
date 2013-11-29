import requests
import bitmethods
import bitchangesets
import bitstats
import simplejson as json


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
    """
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
        # Example: {DrkSephy: 9, Jorge Yau: 15}
        return tally


def iterate_changesets(user, repo, auth_tokens, start, limit=50):
    """
    Gets all of the commit JSON from a repository, bundles it and tallies.
    """
    data = {'changesets_json' : {}}
    num_requests = 0
    iterations = start / limit
    last_request = start % limit

    while num_requests <= iterations:
        if start < limit:
            start = last_request
            limit = last_request
        x = bitstats.tally_changesets(bitchangesets.parse_changesets(
            bitchangesets.get_changesets(user, repo, auth_tokens, limit, start)))
        data['changesets_json'] = bitmethods.dictionary_sum(data['changesets_json'], x)

        start -= limit
        num_requests += 1
    return data


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
    for k,v in data.iteritems():
        devs.append(str(k))
    return devs

def list_commits(data):
    """
    Returns a list of commits in order of developers.
    Useful for D3 graphs.

    Paramters:
        data: Dictionary
            - A dictionary containing commits [keys] to be turned into a list.

    Returns:
        commits: List
            - A list containing the number of commits for each user
              of a given repository.
    """

    commits = []
    for k,v in data.iteritems():
        commits.append(v)
    return commits
