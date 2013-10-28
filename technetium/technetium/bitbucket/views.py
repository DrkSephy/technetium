"""
Views for bitbucket application
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from social.backends.bitbucket import BitbucketOAuth

# Project Modules
import bitauth

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
    social_user = bitauth.get_social_auth_data(request)

    data = { 'user': request.user }
    data['first_name'] = social_user['first_name']
    data['last_name'] = social_user['last_name']
    data['email'] = social_user['email']

    return render(request, 'dashboard.html', data)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

