from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'technetium.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'technetium.views.home'),
    url(r'^done/$', 'technetium.views.done', name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
