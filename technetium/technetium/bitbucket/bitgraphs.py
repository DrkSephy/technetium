"""
Module containing methods for graph generation using Django D3.
This module contains methods for generating pie graphs and
line graphs, with bar charts to come in the near future.
"""
import technetium.bitbucket.bitmethods as bitmethods
import technetium.bitbucket.bitstats as bitstats


def list_xy_data(tallies, datatype):
    """
    Returns a list of data in order of developers.
    Strips out empty set elements.
    x-axis is list of users
    y-axis is list of numeric values

    Parameters:
        tallies: Dictionary
        datatype: String

    Returns:
        Tuple (of Lists)
    """
    xdata, ydata  = [], []
    for key, value in tallies.iteritems():
        series = value[datatype]
        if series:
            xdata.append(key)
            ydata.append(series)
    return xdata, ydata


def set_up_graph(tallies, datatype):
    """
    Sets up simple d3 graph from given chart data

    Parameters:
        tallies: Dictionary
        datatype: String ('changesets', 'issues_completed')

    Returns:
        content: Dictionary
    """
    # Determine container type, leave spaces
    chart_type = 'pieChart'
    container  = 'piechart_container'
    activity   = ' commits'
    if datatype == 'issues_completed':
        chart_type = 'discreteBarChart'
        container = 'discretebarchart_container'
        activity = ' issues completed'

    # Get x and y list data, and set up graphs
    xdata, ydata = list_xy_data(tallies, datatype)
    extra_serie = {"tooltip": {"y_start": "", "y_end": activity}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}

    return {
        'charttype': chart_type,
        'chartdata': chartdata,
        'chartcontainer': container,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }}


def commits_linegraph(changesets=None, count=50):
    """
    Bitbucket has a inconsistent design where if your repo has
    less than 50 commits, they are returned in oldest commits first.
    If your repo has more than 50 commits, the commits are returned
    in most recent commits first.

    Algorithm to parse commits linegraph
    1. Get the timestamp of first and most recent commit
    2. Split the x-axis regions into date ranges
    3. For each commit, parse each user's timestamp to unix time
    4. Create a data series for each user based on date ranges

    Improvements:
    ** [done] Fix nb_element issue
    1. [done] Refactoring into smaller functions
    2. [done] Optimize number of elements

    ** Fix backwards order of linegraph for < 50 commits
    ** Fix cutoff date end
    3. Improve search algorithm

    Returns:
        Dictionary
    """
    # Fixed issues with count of 1 or less
    if not count:
        return {}

    # Initialize start and end timestamp
    start_time, end_time = 0, 0

    # Handle bitbucket's inconsistent commits ordering
    if count <= 50:
        start_time = bitmethods.to_unix_time(changesets[0]['timestamp'])
        end_time = bitmethods.to_unix_time(changesets[-1]['timestamp'])
    else:
        start_time = bitmethods.to_unix_time(changesets[-1]['timestamp'])
        end_time = bitmethods.to_unix_time(changesets[0]['timestamp'])

    # Set limit on amount of time regions
    nb_element = (end_time-start_time)/(86400*1000)
    if nb_element > 60:
        nb_element = 60
    elif nb_element < 10:
        nb_element = 10

    # Get xdata for time range of commits
    step = (end_time - start_time) / nb_element
    xdata = [x for x in range(start_time, end_time, step)]

    # Get commit data with user as its own y data
    user_commits = get_commit_data_of_user(changesets)
    user_series = tally_data_series(xdata, user_commits, nb_element)

    tooltip_date = "%b %d %Y"
    extra_serie = {"tooltip": {"y_start": "Pushed ", "y_end": " commits"},
                    "date_format": tooltip_date}

    # Add each user commit breakdown into chart data
    chartdata = {'x': xdata, 'extra1': extra_serie }
    user_count = 0
    for user in user_series:
        user_count += 1
        ydata = user_series[user]
        string_count = str(user_count)
        chartdata['name'+string_count] = user
        chartdata['y'+string_count] = ydata
        chartdata['extra'+string_count] = extra_serie

    charttype = "lineChart"
    chartcontainer = 'linechart_container'

    return {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%b %d',
            'tag_script_js': True,
            'jquery_on_ready': False,
            }}


def get_commit_data_of_user(changesets):
    """
    Parses commits into individual user commits with
    parsed timestamps. Helper function for commits_linegraph()
    """
    user_commits = {}
    for commit in changesets:
        author = commit['parsed_author']
        timestamp = bitmethods.to_unix_time(commit['timestamp'])
        if author not in user_commits:
            user_commits[author] = []
        user_commits[author].append(timestamp)
    return user_commits


def tally_data_series(xdata, user_timestamps, elements):
    """
    Tallies data series against timestamps.
    Helper function for commits_linegraph()

    Parameters:
        user_timestamps: Dictionary

    Returns:
        Dictionary
    """
    user_series = {}
    for user in user_timestamps:
        # Initialize tallies of each range to 0
        user_series[user] = [0 for x in range(elements)]

        # Cycle through each user's commits
        for timestamp in user_timestamps[user]:
            current, next = 0, 0
            for i in xrange(elements):
                try:
                    current, next = xdata[i], xdata[i+1]
                    if current <= timestamp < next:
                        user_series[user][i] += 1
                        break
                except IndexError:
                    user_series[user][-1] += 1
                    break
    return user_series
