"""
Module for Bitbucket issues aggregation.

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


def get_issues():
    """
    Obtains a JSON dictionary of issues.
    """

    
    r = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/?limit=2')

    


def parse_issues():
    """
    Parses returned JSON data for the API call to the 
    `repositories` endpoint on Bitbucket.
    """
    
    # Get issue data from Bitbucket
    # Can set parameters for query, here the returned list 'limit' = 2
    r = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/?limit=2')

    # Convert python object `r` to JSON string
    d = json.loads(r.text)

    # Key-value pairs to extract.
    # Currently not sure how to extract key-values from nested dictionaries.

    req = ['count','issues']

    # Prints the new dictionary of wanted values
    print dict([i for i in d.iteritems() if i[0] in d and i[0] in req])





