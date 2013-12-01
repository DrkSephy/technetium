"""
Module containing methods for handling repository subscriptions. These
methods include retrieving subscription data from the database, as well
as supplying functionality for subscribe/unsubscribe to any read-access
enabled repository.
"""

from django.db import IntegrityError, DatabaseError
from technetium.bitbucket.models import Subscription
import technetium.bitbucket.bitmethods as bitmethods


def get_list_of_repositories(auth_tokens):
    """
    Returns a list of all repositories that the
    user has at least read access permissions.

    Parameters:
        auth_tokens: OAuth1

    Returns: 
        List
    """
    req_url = "https://bitbucket.org/api/1.0/user/repositories/dashboard/"
    return bitmethods.send_bitbucket_request(req_url, auth_tokens)


def get_all_subscriptions(user):
    """
    Returns a list of all Subscription objects that
    a user is currently subscribed to.

    Parameters:
        user: User (Django Request)

    Returns: 
        List
    """
    return Subscription.objects.filter(user=user).filter(subscribed=True)


def get_repo_id_from_subscriptions(subscriptions):
    """
    Returns a list of repo_ids of repositories that
    a user is subscribed to.

    Parameters:
        subscriptions: Subscription (Object)

    Returns: 
        List (of Integers)
    """
    repo_ids = []
    for repo in subscriptions:
        repo_ids.append(repo.repo_id)
    return repo_ids


def get_subscribed_repo_urls(subs, endpoint, limit):
    """
    Creates a list of all subscribed repo API request URLs
    for issues endpoint.

    Parameters:
        subs: List (Subscription Objects)
        endpoint: String (API request endpoint: 'issues')
        limit: Integer (20)

    Returns: 
        List (String URLs)
    """
    repo_urls = []
    for repo in subs:
        repo_urls.append(bitmethods.make_req_url(
            repo.owner, repo.slug_url, endpoint, limit))
    return repo_urls


def parse_repositories(repositories, repo_ids):
    """
    Parse list of repositories.

    Parameters:
        repositories: List
        repo_ids: List (repo ids that uer is subscribed to)

    Returns: 
        List
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

            # Change in ajax-manage.js if you change strings
            repo_data['subscribed'] = 'No'
            repo_data['action'] = 'subscribe'
            if repo_data['repo_id'] in repo_ids:
                repo_data['subscribed'] = 'Yes'
                repo_data['action'] = 'unsubscribe'

            data['repo_list'].append(repo_data)
        parsed_repositories.append(data)
    return parsed_repositories


def subscribe_repository(user, data):
    """
    Inserts new repository to a user's Subscription in database.

    Parameters:
        user: User (Django Model)
        data: request.POST (Django Query dict)

    Returns: 
        Boolean
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
        user: User (Django Model)
        data: request.POST (Django Query dict)

    Returns: 
        Boolean
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


def unsubscribe_all_repositories(user):
    """
    Unsubscribe from all user's repositories

    Paramters:
        user: User (Django Request)

    Returns:
        Boolean
            - True/False based on if the operation was successful.
    """
    try:
        Subscription.objects.filter(user=user).update(subscribed=False)
        return True
    except (DatabaseError, IntegrityError):
        return False
