"""
Module for managing various Bitbucket endpoints.

Handles the following:

    - Allows method to add repositories.
    - Allows method to remove repositories.
    - Allows flush method to remove all repositories.
"""
import bitmethods
import requests


def get_list_of_repositories(auth_tokens):
    """
    Returns a list of all repositories that the
    user has at least read access permissions.

    Parameters:
    - auth_tokens: OAuth1

    Returns: List
    """
    req_url = "https://bitbucket.org/api/1.0/user/repositories/dashboard/"
    return bitmethods.send_bitbucket_request(req_url, auth_tokens)


def parse_all_repositories(repositories):
    """
    Parse list of repositories.

    Parameters:
    - repositories: List

    Returns: List
    """
    parsed_repositories = []

    for user in repositories:
        user_repos = []
        account_info = user[0]
        repo_list = user[1]


def add_repository():
    """
    Adds a repository to a list which is `followed`
    by the user.

    Parameters:
    -----------
    Repo_slug: string
        - The repository endpoint to add to the list.


    Returns:
    --------
    Confirmation: Boolean
        - Returns true/false based on if operation was successful.

    """

    pass

def remove_repository():
    """
    Removes a repository from a list which is being
    `followed` by the user.

    Paramters:
    ---------
    Repo_slug: string
        - The repository endpoint to remove from the list.

    Returns:
    --------
    Confirmation: Boolean
        - Returns true/false based on if operation was successful.
    """

    pass

def remove_all_repositories():
    """
    Removes all repositories being `followed`.

    Paramters:
    ---------
    Repositories: dictionary
        - A dictionary containing the list of repositories
          to remove.

    Returns:
    -------
    Repository_count: int
        - Integer number of removed repositories.
    """

    pass

