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

    Function will be refactored into sub functions.
    Search can be improved with binary search

    Returns:
        Dictionary
    """
    # Set start date to earliest commit
    start_time = bitmethods.to_unix_time(changesets[-1]['timestamp'])
    end_time = bitmethods.to_unix_time(changesets[0]['timestamp'])
    nb_element = 30

    # Get xdata for time range of commits
    step = (end_time - start_time) / nb_element
    xdata = [x for x in range(start_time, end_time, step)]

    # Get commit data with user as its own y data
    user_commits = {}
    for commit in changesets:
        author = commit['parsed_author']
        timestamp = bitmethods.to_unix_time(commit['timestamp'])
        if author not in user_commits:
            user_commits[author] = []
        user_commits[author].append(timestamp)

    # Create a data series tally for each user
    user_series = {}
    for user in user_commits:
        user_series[user] = [0 for x in range(nb_element)]
        # Cycle through each user's commits
        for timestamp in user_commits[user]:
            for i in xrange(nb_element):
                current = xdata[i]
                next = xdata[i+1]
                if current <= timestamp < next:
                    user_series[user][i] += 1

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
