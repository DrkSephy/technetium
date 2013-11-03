"""
Views for bitbucket application
"""
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from social.backends.bitbucket import BitbucketOAuth

import random
import datetime
import time

# Project Modules
import bitauth
import bitissues
import bitmanager
import bitchangesets

# Home page view
def home(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')

    return render(request, 'home.html', {
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    })


@login_required
def dashboard(request):
    """
    Render dashboard overview
    """

    # Repository to get information from
    user = 'technetiumccny'
    repo = 'technetium'

    # Dictionary to store data
    data = {}

    # OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Render the last 5 issues
    data['issues_json'] = bitissues.parse_issues(request,
        bitissues.get_issues(user, repo, auth_tokens, 5))

    # Render the last 5 changesets
    data['changesets_json'] = bitchangesets.parse_changesets(
        bitchangesets.get_changesets(user, repo, auth_tokens, 5))

    return render(request, 'dashboard.html', data)


@login_required
def dashboard_issues(request):
    """
    Render dashboard issues overview.
    """
    # Example repository
    user = 'technetiumccny'
    repo = 'technetium'
    data = {}

    limit = 13
    filterNameValues={}
    for n, v in request.GET.iteritems():
        filterNameValues[n] = v
        limit += 50

    data['filterNameValues'] = filterNameValues

    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # We need to parse this before in the future
    data['first_name'] = auth_data['first_name']
    data['last_name'] = auth_data['last_name']
    data['email'] = auth_data['email']
    data['issues_json'] = bitissues.parse_issues(request,
        bitissues.get_issues(user, repo, auth_tokens, limit))

    return render(request, 'dashboard_issues.html', data)


@login_required
def dashboard_changesets(request):
    """
    Render changesets on dashboard overview
    """

    # Repository to get changesets from
    user = 'technetiumccny'
    repo = 'technetium'
    data = {}

    # Get the OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Data to render
    data['changesets_json'] = bitchangesets.parse_changesets(
        bitchangesets.get_changesets(user, repo, auth_tokens, 13))

    # Send request to templates
    return render(request, 'dashboard_changesets.html', data)

@login_required
def line_chart(request):
    """
    Render line chart on dashboard
    """
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
    chartcontainer = 'linechart_container' # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }

    return render_to_response('line_chart.html', data)


@login_required
def manage_repositories(request):
    """
    Renders manage repositories page
    """
    data = {}
    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Get and Parse list of all repositories
    data['repositories'] = bitmanager.parse_all_repositories(
        bitmanager.get_list_of_repositories(auth_tokens))
    return render(request, 'manage.html', data)


@login_required
def subscribe_repository(request):
    """
    Handles request to subscribe to a repository
    """
    return HttpResponse("Subscribing to repo")


@login_required
def unsubscribe_repository(request):
    """
    Handles request to unsubscribe from a repository
    """
    return HttpResponse("Unsubscribe from a repo")



@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

