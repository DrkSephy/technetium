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
    # Example
    user = 'technetiumccny'
    repo = 'technetium'
    endpoint = 'issues'

    # Construct URL to get a limit of 5 issues
    req_url = bitmethods.make_req_url(user, repo, endpoint, 5)

    # Get OAuth tokens
    auth_data = bitauth.get_social_auth_data()

    return render(request, 'dashboard.html', data)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

