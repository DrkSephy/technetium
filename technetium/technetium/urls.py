from django.conf.urls import patterns, include, url
from django.contrib import admin

# Import project apps
from bitbucket import views as views_bitbucket

# Uncomment below to enable admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Technetium: bitbucket app URLs
    url(r'^$', views_bitbucket.home),
    url(r'^login/$', views_bitbucket.home),
    url(r'^logout/$', views_bitbucket.logout),
    url(r'^dashboard/$', views_bitbucket.dashboard),

    # Manage Repository views
    url(r'^manage/$', views_bitbucket.manage_repositories),
    url(r'^subscribe/$', views_bitbucket.manage_repositories),
    url(r'^unsubscribe/$', views_bitbucket.manage_repositories),

    # Social Auth URLs
    url(r'', include('social.apps.django_app.urls', namespace='social'))

    # Admin URL
    # url(r'^admin/', include(admin.site.urls)),

)
