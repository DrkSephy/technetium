"""
Module for Bitbucket changesets aggregation.

Proposed methods:
    - GETs changesets for a given repository
    - GETs changesets for multiple repositories.
    - Parses returned JSON.
"""

import requests


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
