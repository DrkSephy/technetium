from django.conf.urls import patterns, include, url
from django.contrib import admin

# Import project apps
from bitbucket import views as views_bitbucket

# Uncomment below to enable admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views_bitbucket.home),

    url(r'^login/$', views_bitbucket.home),
    url(r'^done/$', views_bitbucket.done, name='done'),

    # Social Auth
    url(r'', include('social.apps.django_app.urls', namespace='social'))

    # Admin URL
    # url(r'^admin/', include(admin.site.urls)),

)
