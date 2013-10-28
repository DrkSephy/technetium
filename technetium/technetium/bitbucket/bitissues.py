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
import simplejson as json
import requests
import bitmethods

def get_issues(username, repository, limit=5):
    """
    Obtains a JSON dictionary of issues.

    Parameters:
    - username: String
    - repository: String (repository slug)
    - limit: Integer

    Returns => List
    """
    req_url = bitmethods.make_req_url(username, repository, 'issues', limit)
    req = requests.get(req_url)

    # Success status 200, return JSON
    if req.status_code == 200:
        return json.loads(req.content)['issues']
    return []



def parse_issues(dictionary):
    """
    Parses returned JSON data for the API call to the
    `repositories` endpoint on Bitbucket.

    Parameters:
    ----------
    dictionary: A JSON dictionary to parse
    """


    # Convert python object `r` to JSON string
    json_string = json.loads(dictionary)

    # DAVID'S COMMENTS FOR JORGE:

    # Note: I took a look at the JSON returned from bitbucket. It is valid.

    # Parsing idea: We want to extract only certain key-value pairs.
    # First, convert the json_string to a python dictionary, then
    # we can create an array of keys to look for, and extract them
    # as we iterate through the dictionary.

    # BLOCKER: I'm currently not sure how to extract key/value pairs from
    # a python dictionary which contains both nested/not-nested dictionaries.

    req = ['count','issues']

    # Prints the new dictionary of wanted values. Currently does not
    # extract values from nested dictionaries.
    print dict([i for i in json_string.iteritems() if i[0] in json_string and i[0] in req])


if __name__ == '__main__':
    print get_issues('DrkSephy', 'smw-koopa-krisis')