"""
Views for bitbucket application
"""
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from social.backends.bitbucket import BitbucketOAuth

# Home page view
def home(request):
    if request.user.is_authenticated():
        return redirect('/done')

    return render('home.html', {
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    })


@login_required
def done(request):
    return render(request, 'done.html', {
      'user': request.user,
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    })
