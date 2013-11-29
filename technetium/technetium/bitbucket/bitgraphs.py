"""
Module for bitgraphs
"""
import bitstats

def commits_pie_graph(chart_data):
    """
    Sets up pie chart from given chart data

    Parameters:
        chart_data: Dictionary

    Returns:
        content: Dictionary
    """
    # Get x and y list data
    xdata = bitstats.list_users(chart_data)
    ydata = bitstats.list_commits(chart_data)

    # Setup Graph Parameters
    extra_serie = {"tooltip": {"y_start": "", "y_end": "commits"}}
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

