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
    Temporary placeholder for line graph code.

    David's notes
    -------------
    I'll need to figure out how to properly get the data from the JSON
    returned from Bitbucket, and get it into the proper form. Will
    probably need a few methods from bitstats to get the data in the
    right form and pass it into the charting views.
    """
    # Set start date to earliest commit
    start_time = bitmethods.to_unix_time(changesets[-1]['timestamp'])
    end_time = bitmethods.to_unix_time(changesets[0]['timestamp'])
    nb_element = (end_time-start_time) / (86400*1000)
    print nb_element

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


    tooltip_date = "%b %d %Y %H:%M:%S %p"
    extra_serie = {"date_format": tooltip_date}

    # Add each user commit breakdown into chart data
    chartdata = {'x': xdata, 'extra1': extra_serie }
    user_count = 0
    for user in user_commits:
        ydata = [random.randint(0, 10) for i in range(nb_element)]
        user_count += 1
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
