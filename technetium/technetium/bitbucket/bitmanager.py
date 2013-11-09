"""
Module for managing various Bitbucket endpoints.

Handles the following:

    - Allows method to subscribe to repositories.
    - Allows method to unsubscribe from repositories.
    - Allows flush method to unsubscribe all repositories.
"""
from models import Subscription
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


def get_all_subscriptions(user):
    """
    Returns a list of all Subscription objects that
    a user is currently subscribed to.

    Parameters:
    - user: User (Django Request)

    Returns: List
    """
    return Subscription.objects.filter(user=user).filter(subscribed=True)


def get_repo_id_from_subscriptions(subscriptions):
    """
    Returns a list of repo_ids of repositories that
    a user is subscribed to.

    Parameters:
    - subscriptions: Subscription (Object)

    Returns: List (of Integers)
    """
    repo_ids = []
    for repo in subscriptions:
        repo_ids.append(repo.repo_id)
    return repo_ids


def parse_repositories(repositories, subscriptions):
    """
    Parse list of repositories.

    Parameters:
    - repositories: List
    - subscriptions: List (of Repo IDs)

    Returns: List
    """
    parsed_repositories = []
    for user in repositories:
        # Leave account information as it is
        data = {'account_info' : user[0]}
        data['repo_list'] = []

        # Parse and add information to repository list
        for repo in user[1]:
            repo_data = {}
            repo_data['name'] = repo['name']
            repo_data['url_path'] = repo['absolute_url']
            repo_data['full_url'] = 'https://bitbucket.org' + repo_data['url_path']
            repo_data['repo_id'] = repo['_pk']
            repo_data['owner'] = repo['owner']
            repo_data['slug'] = repo['slug']
            data['repo_list'].append(repo_data)
        parsed_repositories.append(data)
    return parsed_repositories


def subscribe_repository(user, data):
    """
    Inserts new repository to a user's Subscription in database.

    Parameters:
    - user: User (Django Model)
    - data: request.POST (Django Query dict)

    Returns: Boolean
    - True/False based on if operation was successful.
    """
    # If subscription exists, update subscribed to True
    subscription = Subscription.objects.filter(user=user).filter(repo_id=data['repo-id'])
    if subscription:
        subscription[0].subscribed = True
        subscription[0].save()

    # Subscription doesn't exist, insert new subscription
    else:
        subscription = Subscription(
            user=user,
            repo_id = data['repo-id'],
            repository = data['repo-name'],
            slug_url = data['repo-slug'],
            owner = data['repo-owner'],
            subscribed = True )
        subscription.save()

    # Return status of subscription
    if subscription:
        return True
    return False


def unsubscribe_repository(user, data):
    """
    Updates a user's Subscription in database and set
    subscribed to False.

    Parameters:
    - user: User (Django Model)
    - data: request.POST (Django Query dict)

    Returns: Boolean
    - True/False based on if operation was successful.
    """
    # If subscription exists, update subscribed to False
    subscription = Subscription.objects.filter(user=user).filter(repo_id=data['repo-id'])
    if subscription:
        subscription[0].subscribed = False
        subscription[0].save()
        return True
    else:
        return False


def unsubscribe_all_repositories():
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

