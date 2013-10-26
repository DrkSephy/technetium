"""
Module for Bitbucket changesets aggregation.

Proposed methods:
    - GETs changesets for a given repository
    - GETs changesets for multiple repositories.
    - Parses returned JSON.

Bitbucket API requests start at the following endpoint:

https://bitbucket.org/api/1.0/repositories/
and have the following layout:

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

import requests
import simplejson as json


def get_changesets(URL):
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
    r = requests.get(URL)
   
    # Return the JSON
    return r.text

    

def parse_changesets(dictionary):
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
    json_string = json.loads(dictionary)

    # Keys that we are interested in
    # Currently does not work for nested key/value pairs.
    req = ['count', 'changests', 'author', 'date']

    print dict([i for i in json_string.iteritems() if i[0] in json_string and i[0] in req])

