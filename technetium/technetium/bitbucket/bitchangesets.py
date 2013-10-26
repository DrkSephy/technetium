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


def get_changesets():
    """
    Obtains a JSON dictionary of changesets across
    a repository/repositories.



    Parameters:
    ----------


    Returns:
    -------
    changesets: dictionary
        - A dictionary containing [key][values] representing
          all commits for the requested repositories.
    """
    

def parse_changesets():
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
    pass
