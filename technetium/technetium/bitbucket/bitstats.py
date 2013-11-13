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

def list_users(data):
    """
    Returns a list of all developers in a repository.
    Useful for plugging directly into the Pie Chart.
    """

    devs = []
    for k,v in data.iteritems():
        devs.append(k)
    return devs


