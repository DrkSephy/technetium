"""
Views for bitbucket application
"""
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from social.backends.bitbucket import BitbucketOAuth

# Project Modules
import bitauth
import bitissues
import bitmanager

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
    Render dashboard overview.
    """
    # Example repository
    user = 'technetiumccny'
    repo = 'technetium'
    data = {}

    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)

    # We need to parse this before in the future
    data['first_name'] = auth_data['first_name']
    data['last_name'] = auth_data['last_name']
    data['email'] = auth_data['email']
    data['issues_json'] = bitissues.parse_issues(bitissues.get_issues(user, repo, auth_tokens, 13))
    return render(request, 'dashboard.html', data)


@login_required
def dashboard_changesets(request):
    """
    Render changesets on dashboard overview
    """


@login_required
def manage_repositories(request):
    """
    Renders manage repositories page
    """
    data = {}

    # Get OAuth tokens, starting to seem WET
    auth_data = bitauth.get_social_auth_data(request.user)
    auth_tokens = bitauth.get_auth_tokens(auth_data)
    data['all_repos'] = bitmanager.get_list_of_repositories(auth_tokens)
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

