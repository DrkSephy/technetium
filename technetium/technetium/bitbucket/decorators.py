"""
Decorators for bitbucket views
"""
from django.utils.functional import wraps
from django.core import serializers
import bitmanager

def load_subscriptions(function):
    """
    Decorator to wrap request session with subscription info.
    """
    def wrapper(request, *args, **kwargs):
        subscriptions = bitmanager.get_all_subscriptions(request.user)
        data = serializers.serialize("json", subscriptions)
        request.session['subscriptions'] = data
        return function(request, *args, **kwargs)
    return wraps(function)(wrapper)
