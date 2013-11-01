"""
Module for managing various Bitbucket endpoints.

Handles the following:

    - Allows method to add repositories.
    - Allows method to remove repositories.
    - Allows flush method to remove all repositories.
"""
import requests


def get_repositories():
    """
    Gets all repositories that the user owns/has
    access privledges to.

    Parameters:
    -----------

    Returns:
    --------
    repos: dictionary
        - A dictionary containing a list of all
          repositories owned by the user.
    """
    pass


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

