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

    tally = {}
    for i in data:
        for k,v in i.iteritems():
            if v in tally:
                
