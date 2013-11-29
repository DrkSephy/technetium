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
    return render(request, 'dashboard.html', data)


@login_required
def reports(request, owner, repo_slug):
    """
    Render the webpage to show reports and graphs
    """
    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # Tally all of the changesets for each user
    changesets_count = bitchangesets.get_changesets_count(owner, repo_slug, auth_tokens)
    changesets_urls = bitmethods.get_api_urls(owner, repo_slug, 'changesets', changesets_count)
    changesets_parsed = bitchangesets.iterate_all_changesets(changesets_urls, auth_tokens)
    changesets_tallied = bitstats.tally_changesets(changesets_parsed)

    # Tally the number of issues opened, assigned
    issues_count = bitissues.get_issues_count(owner, repo_slug, auth_tokens)
    issues_urls = bitissues.get_issues_urls(owner, repo_slug, 'issues', issues_count)
    issues_parsed = bitstats.parse_issues_for_tallying(issues_urls, auth_tokens)
    issues_tallied = bitstats.tally_issues(issues_parsed)

    # Combine tallies for issues and changesets for each user
    tallies = bitstats.combine_tallies(changesets_tallied, issues_tallied)

    # Get retrieved context from subscribed repositories
    subscribed = bitmanager.get_all_subscriptions(request.user)
    context = bitmethods.package_context(subscribed)
    context['owner'] = owner
    context['repo_slug'] = repo_slug
    context['tallies'] = tallies
    context['commits_piegraph'] = bitgraphs.commits_pie_graph(tallies)
    return render(request, 'statistics.html', context)


@login_required
def dashboard_issues(request):
    """
    Render dashboard issue tracker overview.
    """
    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

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
    req_url = bitmethods.make_req_url(repo_owner, repo_slug, 'issues', 10, repo_count)
    raw_data = [bitmethods.send_bitbucket_request(req_url, auth_tokens)]
    parsed_data = bitissues.parse_issues(raw_data[0]['issues'])
    html_data = bitissues.add_html_issue_rows(parsed_data)
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
