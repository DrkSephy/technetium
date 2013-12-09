"""
Module contains functions for dashboard
"""

def get_screenshots(num_screenshots=5):
    """
    Returns a list of screenshot dictionary elements.

    Parameters:
        - num_screenshots: Integer

    Returns:
        List
    """
    descriptions = [
        "Repository Subscription Manager",
        "Centralized Issue Tracker",
        "Repository Commits and Issues Report",
        "Commit History Linegraph",
        "Graphs of Contribution Breakdown",
    ]

    screenshots = []
    for i in range(num_screenshots):
        data = {}
        data['id'] = i
        data['filename'] = "/static/img/screenshots/screenshot-%d.jpg" % i
        data['description'] = descriptions[i]
        screenshots.append(data)
    return screenshots