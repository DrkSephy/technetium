"""
Views for bitbucket application
"""
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from social.backends.bitbucket import BitbucketOAuth
import random
import datetime
import time

# Project Modules
import bitauth
import bitissues
import bitfilter
import bitmanager
import bitchangesets
import bitmethods
import bitstats

# Home page view
def home(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')

    return render(request, 'home.html', {
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    })


@login_required
def statistics(request):
    """
    Render the reports.
    """
    # Using smw-koopa-krisis as a test repository
    user = 'DrkSephy'
    repo = 'smw-koopa-krisis'

    # Store the data
    data = {}
    # OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    data['changesets_json'] =   bitstats.tally_changesets(bitchangesets.parse_changesets(
        bitchangesets.get_changesets(user, repo, auth_tokens, 50)))

    return render(request, 'statistics.html', data)


@login_required
def dashboard(request):
    """
    Render dashboard overview. It will contain the following:
    1. Issue Tracker reports
    2. Changeset reports
    3. Progress reports
    4. Charts and graphs
    """
    # Get retrieved issues from subscribed repositories
    subscribed  = bitmanager.get_all_subscriptions(request.user)
    data = bitmethods.package_context(subscribed)
    return render(request, 'dashboard.html', data)


@login_required
def dashboard_issues(request):
    """
    Render dashboard issue tracker overview.
    """
    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Get all subscribed repositories
    limit = 10
    subscribed  = bitmanager.get_all_subscriptions(request.user)
    repo_urls   = bitmanager.get_subscribed_repo_urls(subscribed, 'issues', limit)
    repo_issues = bitissues.parse_all_issues(
                  bitissues.get_issues_from_subscribed(repo_urls, auth_tokens))
    issues_list = bitissues.attach_meta(subscribed, repo_issues)
    print issues_list
    # Get retrieved issues from subscribed repositories
    data = bitmethods.package_context(subscribed)
    data['issues_list'] = issues_list
    return render(request, 'dashboard_issues.html', data)


@login_required
def line_chart(request):
    """
    Render line chart on dashboard/graphs

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
    return render(request,'line_chart.html', data)



@login_required
def pie_chart(request):
    """
    Render pie chart on dashboard/graphs
    """

    # Pie charts take strings on the x-axis,
    # and the distribution are integers on the y-axis.
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container' # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'pie_chart.html', data)


#######################
# MANAGE REPOSITORIES #
#######################
@login_required
def manage_repositories(request):
    """
    Renders manage repositories page
    """
    # Get OAuth tokens
    auth_data   = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Get subscriptions and Parse list of all repositories
    subscribed = bitmanager.get_all_subscriptions(request.user)
    repo_ids = bitmanager.get_repo_id_from_subscriptions(subscribed)
    repositories  = bitmanager.get_list_of_repositories(auth_tokens)

    # Package subscribed
    data = bitmethods.package_context(subscribed)
    data['repositories'] = bitmanager.parse_repositories(repositories, repo_ids)
    return render(request, 'manage.html', data)


@login_required
def subscribe_repository(request):
    """
    [AJAX] Handles request to subscribe to a repository.
    Content should contain a dictionary with the
    fields for Subcription Model.
    """
    print "Subscribing to %s: %s" % \
        (request.POST['repo-id'], request.POST['repo-name'])

    # Success: subscribe to repository
    if bitmanager.subscribe_repository(request.user, request.POST):
        return HttpResponse("{'status' : 'sucess'}")
    return HttpResponse("{'status' : 'fail'}")


@login_required
def unsubscribe_repository(request):
    """
    [AJAX] Handles request to unsubscribe from a repository
    """
    print "Unsubscribing from %s: %s" % \
        (request.POST['repo-id'], request.POST['repo-name'])

    # Success: unsubscribe from repository
    if bitmanager.unsubscribe_repository(request.user, request.POST):
        return HttpResponse("{'status' : 'sucess'}")
    return HttpResponse("{'status' : 'fail'}")


@login_required
def unsubscribe_all(request):
    """
    Handles request to unsubscribe from a repository
    """
    bitmanager.unsubscribe_all_repositories(request.user)
    return redirect('/manage')


@login_required
def fetch_more_issues(request):
    """
    [AJAX] Handles request to  from a repository
    """
    # Get OAuth tokens
    auth_data   = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)
    repo_owner = request.GET['repo-owner']
    repo_slug  = request.GET['repo-slug']
    repo_count = int(request.GET['count'])

    # Filter out just one repo slug
    req_url = bitmethods.make_req_url(repo_owner, repo_slug, 'issues', 15, repo_count)
    raw_data = [bitmethods.send_bitbucket_request(req_url, auth_tokens)]
    parsed_data = bitissues.parse_issues(raw_data[0]['issues'])
    html_data = bitissues.add_html_issue_rows(parsed_data)
    return HttpResponse(html_data)


##################
# AUTHENTICATION #
##################
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

