"""
Module for Bitbucket changesets aggregation.
"""

import requests
import simplejson as json
import bitmethods


def get_changesets(user, repo, auth_tokens, limit):
    """
    Obtains a JSON dictionary of changesets across
    a repository/repositories.

    Parameters:
    -----------
    URL: string
        - The url to GET the resource from bitbucket.

    Returns:
    -------
    changesets: dictionary
        - A dictionary containing [key][values] representing
          all commits for the requested repositories.
    """

    # Get the changesets.
    # The URL for changesets is:
    # 'https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/changesets/?limit=2')
    req_url = bitmethods.make_req_url(user, repo, 'changesets', limit)
    changesets = bitmethods.send_bitbucket_request(req_url, auth_tokens)
    return changesets['changesets']
   
    # Return the JSON

    

def parse_changesets(changesets):
    """
    Parses returned JSON data for the API call to the
    `repositories` endpoint on Bitbucket.

    Parameters:
    -----------
    Repositories: dictionary
        - A dictionary containing repository JSON
          which needs to be parsed for all useful
          information.

    Returns:
    --------
    changeset_data: dictionary
        - A JSON formatted dictionary containing 
          all relevant data.
    """

    x = changesets['changesets']

    keys = ['author', 'branch', 'utctimestamp', 'message']

    changeset = []

    for a in x:
        new_list = {}
        for k,v in a.iteritems():
            if k in keys:
                new_list[k] = v
        changeset.append(new_list)

    return changeset

