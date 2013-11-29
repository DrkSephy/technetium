import requests
import simplejson as json
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


def parse_changesets(repository):
    """
    Parses returned JSON data for the API call to the
    `repositories` endpoint on Bitbucket.

    Parameters:
        repositories: dictionary
            - A dictionary containing JSON from a repository
              which needs to be parsed for all useful
              information.
    """

    keys = ['raw_author']

    changeset = []

    for a in repository:
        new_list = {}
        for k,v in a.iteritems():
            if k in keys:
                if re.match('(.*?)(?=\s<)', v) == None:
                    new_list[k] = v
                else:
                    v2 = re.match('(.*?)(?=\s<)', v)
                    new_list[k] = v2.group()
        changeset.append(new_list)

    return changeset

