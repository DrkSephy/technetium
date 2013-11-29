"""
Module for bitgraphs
"""
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
    # Get random data
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 150
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
                   "date_format": tooltip_date}
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
                 'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}

    charttype = "lineChart"
    chartcontainer = 'linechart_container'

    return {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
            }}
