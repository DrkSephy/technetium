from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from social.backends.bitbucket import BitbucketOAuth

# Home page view
def home(request):
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {
      'key': getattr(settings, 'SOCIAL_AUTH_BITBUCKET_KEY', None)
    }, Request.Context(request))


