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
    print data['issues_json']
    return render(request, 'dashboard.html', data)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

