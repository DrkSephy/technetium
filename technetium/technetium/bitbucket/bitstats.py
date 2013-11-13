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

    # Dictionary to store commit counts
    tally = {}
    # Iterate over all dictionaries in our list
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
