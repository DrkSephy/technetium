import simplejson as json
from datetime import datetime
from collections import defaultdict
import requests
import grequests


#######################
# BITBUCKET CONSTANTS #
#######################
API_BASE_URL = "https://bitbucket.org/api/1.0/repositories/"
BITBUCKET_BASE_URL = "https://bitbucket.org/"


def make_req_url(user, repo, endpoint, limit=50, start=0):
    """
    Constructs a URL for bitbucket API request.

    Parameters:
        user: String
            - The Bitbucket username.
        repo: String
            - The Bitbucket repository name.
        endpoint: String
            - The Bitbucket API endpoint.
        limit: Integer (Max 50)
            - The number of data entries to return.
        start: Integer
            - The starting node number for the resource.

    Returns:
        url: String
            - The URL to send the request to.
    """
    url = "%s%s/%s/%s" % (API_BASE_URL, user, repo, endpoint)

    # Set limit is given and is above 50, set limit to 50
    if limit and limit > 50:
        limit = 50

    # Handle extra queries
    url += "?limit=%d&start=%d" % (limit, start)
    return url


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


def dictionary_sum(dict_a, dict_b):
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
    # New dictionary to store merged dict
    dicts = defaultdict(int, dict_a)
    # For all key-value pairs in dict B, sum up values
    # In the new dictionary.
    for key, value in dict_b.items():
        # Sum values corresponding to keys
        dicts[key] += value
    return dict(dicts)


