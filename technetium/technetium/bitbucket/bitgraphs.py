"""
Module for bitgraphs
"""
import bitmethods
import bitstats
import random
import datetime
import time


def commits_pie_graph(tallies):
    """
    Sets up pie chart from given chart data

    Parameters:
        tallies: Dictionary

    Returns:
        content: Dictionary
    """
    # Get x and y list data
    xdata = bitstats.list_users(tallies)
    ydata = bitstats.list_data(tallies)

    # Setup Graph Parameters
    extra_serie = {"tooltip": {"y_start": "", "y_end": " commits"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'

    return {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }}


def commits_linegraph(changesets=None):
    """
    Algorithm to parse commits linegraph
    1. Get the timestamp of first and most recent commit
    2. Split the x-axis regions into date ranges
    3. For each commit, parse each user's timestamp to unix time
    4. Create a data series for each user based on date ranges

    Improvements:
    ** [done] Fix nb_element issue
    ** Fix cutoff date end
    1. [done] Refactoring into smaller functions
    2. Optimize number of elements
    3. Improve search algorithm
    4. Synch colors of line and pie graphs

    Returns:
        Dictionary
    """
    # Set start date to earliest commit
    start_time = bitmethods.to_unix_time(changesets[-1]['timestamp'])
    end_time = bitmethods.to_unix_time(changesets[0]['timestamp'])+(86400*2000)
    nb_element = 40

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
                current = xdata[i]
                try:
                    next = xdata[i+1]
                    if current <= timestamp < next:
                        user_series[user][i] += 1
                        break
                except IndexError:
                    user_series[user][-1] += 1
                    break
    return user_series
