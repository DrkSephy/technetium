"""
Module containing methods for interacting with changeset data from
Bitbucket. These methods deal with retrieving JSON data and parsing
it for use in Technetium's reports.
"""
import bitmethods
import re


def iterate_all_changesets(req_urls, auth_tokens):
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
    parsed_changesets = []
    if req_urls:
        # Send async requests to get raw changesets
        raw_changesets = bitmethods.send_async_bitbucket_requests(req_urls, auth_tokens)
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
    data['parsed_author'] = re.sub(r'\s*<.+>', '', changeset['raw_author'])
    data['timestamp'] = changeset['timestamp']
    return data

