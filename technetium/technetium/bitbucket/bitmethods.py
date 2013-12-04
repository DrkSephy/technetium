"""
Module bitmethods contains a handful of auxillary methods.
These methods are meant to be used within all other modules.
"""
from datetime import datetime
import simplejson as json
import time
import requests
import grequests


#######################
# BITBUCKET CONSTANTS #
#######################
API_BASE_URL = "https://bitbucket.org/api/1.0/repositories/"
BITBUCKET_BASE_URL = "https://bitbucket.org/"


def make_req_url(user, repo, endpoint, limit=50, queries=None):
    """
    Constructs a URL for bitbucket API request.

    Parameters:
        user: String
            - The Bitbucket username
        repo: String
            - The Bitbucket repository name
        endpoint: String
            - The Bitbucket API endpoint
        queries: Dictionary
            - Additional query set parameters
        limit: Integer (Max 50)
            - The number of data entries to return

    Returns:
        url: String
            - The URL to send the request to.
    """
    url = "%s%s/%s/%s" % (API_BASE_URL, user, repo, endpoint)

    # Set limit is given and is above 50, set limit to 50
    if limit and limit > 50:
        limit = 50
    url += "?limit=%d" % limit

    # Add additional query parameters
    if queries:
        for key in queries:
            url += "&%s=%s" % (key, queries[key])
    return url


def get_api_urls(user, repo, endpoint, start, limit=50):
    """
    Makes a list of api urls based on iterating through limit.

    Returns:
        content: List
    """
    req_urls = []
    queries = {}
    queries['start'] = start
    if start:
        count = 0
        stop = start/limit
        while count <= stop:
            new_url = make_req_url(user, repo, endpoint, limit, queries)
            req_urls.append(new_url)
            queries['start'] -= limit
            count += 1
    return req_urls


def send_bitbucket_request(req_url, auth_tokens):
    """
    Obtains a JSON dictionary from bitbucket API endpoint.

    Parameters:
        req_url: String (URL)
            - The URL to send the request to.
        auth_tokens: OAuth1 (Object)
            - The authentication tokens required for the OAuth1 Protocol.

    Returns:
        content: Dictionary
            - A JSON dictionary from the requested URL.
    """
    # Success status 200, return JSON
    req = requests.get(req_url, auth=auth_tokens)
    if req.status_code == 200:
        return json.loads(req.content)
    return {}


def send_async_bitbucket_requests(req_urls, auth_tokens):
    """
    Use this method to send asynchronous requests for bitbucket
    API when generating reports.

    Parameters:
        req_urls: List (of URLS)
            - The list of URLs to send requests to.
        auth_tokens: OAuth1
            - The authentication tokens required for the OAuth1 protocol.

    Returns:
        content: Dictionary
            - A list of JSON dictionaries from the requested URLs.
    """
    urls = (grequests.get(url, auth=auth_tokens) for url in req_urls)
    json_list = []
    for response in grequests.map(urls):
        try:
            json_list.append(json.loads(response.content))
        except Exception:
            json_list.append({})
    return json_list


def get_count(owner, repo_slug, auth_tokens, endpoint):
    """
    Gets count from endpoint of bitbucket API request

    Returns:
        Integer
    """
    count_url = make_req_url(owner, repo_slug, endpoint, 0)
    response  = send_bitbucket_request(count_url, auth_tokens)
    if response and 'count' in response:
        return response['count']-1
    return 0


def to_unix_time(timestamp):
    """
    Formats a string timestamp to unix seconds.
    Multiplies by 1000 to use for d3.

    Parameters:
        timestamp: String

    Returns:
        Integer
    """
    date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return int(time.mktime(date.timetuple()))*1000


def format_timestamp(timestamp):
    """
    Formats string timestamp into readable timestamp.

    Parameters:
        timestamp: String
            - The timestamp to format.

    Returns:
        timestamp: String
            - The formatted timestamp.
    """
    try:
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S+00:00')
        return datetime.strftime(date, '%m-%d-%Y')
    except ValueError:
        return ''


def package_context(subscriptions):
    """
    Packages common data for request context

    Returns:
        data: Dictionary
            - A dictionary of repositories the user is subscribed to.
    """
    data = {'subscriptions' : subscriptions}
    data['subscription_count'] = len(subscriptions)
    return data


def dictionary_sum(dict_a, dict_b, sum_key):
    """
    Sums the values of two dictionaries based on corresponding keys.

    Parameters:
        dict_a: Dictionary
            - The dictionary to add values to.

        dict_b: Dictionary
            - The second dictionary whose values are iterated through and
              added with the first dictionary.

    Returns:
        dictionary: Dictionary
            - The new dictionary containing the sum of its inputs.
    """
    for key, value in dict_b.items():
        if key not in dict_a:
            dict_a[key] = value
        else:
            dict_a[key][sum_key] += value[sum_key]
    return dict_a

