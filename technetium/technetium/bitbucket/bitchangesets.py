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
    pass

def parse_changesets():
    pass
