"""
Module for bitchangesets
"""
import bitmethods
import re


def get_changesets(user, repo, auth_tokens, limit, start):
    """
    Obtains a JSON dictionary of changesets across
    a repository/repositories.

    Parameters:
        URL: string
            - The url to GET the resource from bitbucket.

    Returns:
        changesets: dictionary
            - A dictionary containing [key][values] representing
              all commits for the requested repositories.
    """
    req_url = bitmethods.make_req_url(user, repo, 'changesets', limit, start)
    res_json = bitmethods.send_bitbucket_request(req_url, auth_tokens)
    if 'changesets'  in res_json:
        return res_json['changesets']
    return {}


def parse_all_changesets(req_urls, auth_tokens):
    """
    Sends async API requests to gets all of the commits
    from a repository based on the req_urls. Parses the
    json reponse and tallies commits for each user.
    Uses parse_changesets as a helper function.

    Parameters:
        req_urls: List

    Returns:
        List
    """
    # Send async requests to get raw changesets
    raw_changesets = bitmethods.send_async_bitbucket_requests(req_urls, auth_tokens)
    parsed_changesets = []
    for changesets in raw_changesets:
        for changeset in changesets['changesets']:
            parsed_changesets.append(parse_changeset(changeset))
    return parsed_changesets


def parse_changeset(changeset):
    """
    Parses returned JSON data for the API call to the
    `repositories` endpoint on Bitbucket.

    Parameters:
        repositories: dictionary
            - A dictionary containing JSON from a repository
              which needs to be parsed for all useful
              information.

    Returns:
        changesets: List
    """
    data = {}
    data['parsed_author'] = re.sub(r'\s+<.+>', '', changeset['raw_author'])
    data['author'] = changeset['author']
    data['timestamp'] = changeset['utctimestamp']
    return data
