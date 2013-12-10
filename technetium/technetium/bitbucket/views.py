"""
Views for bitbucket web application
"""
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Project Modules
import bitauth
import bitissues
import bitmanager
import bitchangesets
import bitmethods
import bitstats
import bitgraphs
import bitfilter
import bitdashboard


# Home page view
def home(request):
    """
    Renders the home login page for technetium
    """
    if request.user.is_authenticated():
        return redirect('/dashboard')

    return render(request, 'home.html', {
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    })


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
    data['screenshots'] = bitdashboard.get_screenshots()
    return render(request, 'dashboard.html', data)


@login_required
def reports(request, owner, repo_slug):
    """
    Render the webpage to show reports and graphs
    """
    # Get OAuth tokens
    auth_tokens = bitauth.get_auth_tokens(request.user)

    # Tally the number of issues opened, assigned
    issues_count = bitmethods.get_count(owner, repo_slug, auth_tokens, 'issues')
    issues_urls = bitissues.get_issues_urls(owner, repo_slug, 'issues', issues_count)
    issues_parsed = bitstats.parse_issues_for_tallying(issues_urls, auth_tokens)
    issues_tallied = bitstats.tally_issues(issues_parsed)

    # Tally issue comments
    issues_comments_urls = bitissues.get_issue_comments_urls(issues_parsed, owner, repo_slug)
    issues_comments = bitmethods.send_async_bitbucket_requests(issues_comments_urls, auth_tokens)
    issues_tallied = bitstats.tally_issue_comments(issues_tallied, issues_comments)
    print issues_tallied
    return

    # Tally all of the changesets for each user
    changesets_count = bitmethods.get_count(owner, repo_slug, auth_tokens, 'changesets')
    changesets_urls = bitmethods.get_api_urls(owner, repo_slug, 'changesets', changesets_count)
    changesets_parsed = bitchangesets.iterate_all_changesets(changesets_urls, auth_tokens)
    changesets_tallied = bitstats.tally_changesets(changesets_parsed)

    # Combine tallies for issues and changesets for each user
    tallies = bitstats.combine_tallies(changesets_tallied, issues_tallied)

    # Get retrieved context from subscribed repositories
    subscribed = bitmanager.get_all_subscriptions(request.user)
    context = bitmethods.package_context(subscribed)
    context['owner'] = owner
    context['repo_slug'] = repo_slug
    context['tallies'] = tallies
    context['commits_piegraph'] = bitgraphs.commits_pie_graph(tallies)
    context['commits_linegraph'] = bitgraphs.commits_linegraph(changesets_parsed, changesets_count)
    context['issues_bargraph'] = bitgraphs.issues_bargraph(tallies)
    return render(request, 'statistics.html', context)


@login_required
def dashboard_issues(request):
    """
    Render dashboard issue tracker overview.
    """
    # Get OAuth tokens
    auth_tokens = bitauth.get_auth_tokens(request.user)

    # Get all subscribed repositories
    subscribed  = bitmanager.get_all_subscriptions(request.user)
    repo_urls   = bitmanager.get_subscribed_repo_urls(subscribed, 'issues', 10)
    repo_issues = bitissues.parse_all_issues(
                  bitmethods.send_async_bitbucket_requests(repo_urls, auth_tokens))
    issues_list = bitissues.attach_meta(subscribed, repo_issues)

    # Get retrieved issues from subscribed repositories
    data = bitmethods.package_context(subscribed)
    data['issues_list'] = issues_list
    return render(request, 'dashboard_issues.html', data)


#######################
# MANAGE REPOSITORIES #
#######################
@login_required
def manage_repositories(request):
    """
    Renders manage repositories page
    """
    # Get OAuth tokens
    auth_tokens = bitauth.get_auth_tokens(request.user)

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
    # Success: subscribe to repository
    if bitmanager.subscribe_repository(request.user, request.POST):
        return HttpResponse(status=201)
    return HttpResponse(status=500)


@login_required
def unsubscribe_repository(request):
    """
    [AJAX] Handles request to unsubscribe from a repository
    """
    # Success: unsubscribe from repository
    if bitmanager.unsubscribe_repository(request.user, request.POST):
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@login_required
def unsubscribe_all(request):
    """
    Handles request to unsubscribe from a repository
    """
    bitmanager.unsubscribe_all_repositories(request.user)
    return redirect('/manage')


#################
# ISSUE TRACKER #
#################
@login_required
def fetch_more_issues(request):
    """
    [AJAX] Handles request to  from a repository
    """
    # Get OAuth tokens
    auth_tokens = bitauth.get_auth_tokens(request.user)
    repo_owner = request.GET['repo-owner']
    repo_slug  = request.GET['repo-slug']
    repo_count = int(request.GET['count'])
    queries = {}
    queries['start'] = repo_count

    if 'filter-type' in request.GET:
        queries['kind'] = request.GET['filter-type']

    if 'filter-status' in request.GET:
        queries['status'] = request.GET['filter-status']

    # Grabs more deal, parses them, and renders template context
    html_data = bitissues.ajax_process_issues(auth_tokens, repo_owner, repo_slug, 10, queries)
    return HttpResponse(html_data)


@login_required
def filter_issues_type(request):
    """
    [AJAX] Grab issues that are filtered by type
    """
    # Get query data from Ajax request
    auth_tokens = bitauth.get_auth_tokens(request.user)
    repo_owner = request.GET['repo-owner']
    repo_slug = request.GET['repo-slug']
    queries = {}
    if 'filter-type' in request.GET:
        queries['kind'] = request.GET['filter-type']

    if 'filter-status' in request.GET:
        queries['status'] = request.GET['filter-status']

    count = 10
    if 'count' in request.GET:
        count = int(request.GET['count'])

    # Create request URL and get filtered issues by kind
    html_data = bitissues.ajax_process_issues(auth_tokens, repo_owner, repo_slug, count, queries)
    return HttpResponse(html_data)


@login_required
def filter_issues_status(request):
    """
    [AJAX] Grab issues that are filtered by status
    """
    # Get query data from Ajax request
    auth_tokens = bitauth.get_auth_tokens(request.user)
    repo_owner = request.GET['repo-owner']
    repo_slug = request.GET['repo-slug']
    queries = {}
    if 'filter-status' in request.GET:
        queries['status'] = request.GET['filter-status']

    if 'filter-type' in request.GET:
        queries['kind'] = request.GET['filter-type']

    count = 10
    if 'count' in request.GET:
        count = int(request.GET['count'])

    # Create request URL and get filtered issues by kind
    html_data = bitissues.ajax_process_issues(auth_tokens, repo_owner, repo_slug, count, queries)
    return HttpResponse(html_data)


##################
# AUTHENTICATION #
##################
@login_required
def logout(request):
    """
    Sends a request to log out user
    """
    auth.logout(request)
    return redirect('/')
