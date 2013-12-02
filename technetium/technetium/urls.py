from django.conf.urls import patterns, include, url
from django.contrib import admin

# Import project apps
from bitbucket import views as views_bitbucket

# Uncomment below to enable admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Technetium: bitbucket app URLs
    url(r'^$', views_bitbucket.home),
    url(r'^login/$', views_bitbucket.home, name='login'),
    url(r'^logout/$', views_bitbucket.logout, name='logout'),

    # Technetium Sidebar
    url(r'^dashboard/$', views_bitbucket.dashboard, name='dashboard'),
    url(r'^issues/$', views_bitbucket.dashboard_issues, name='issues'),
    url(r'^manage/$', views_bitbucket.manage_repositories, name='manage'),
    url(r'^reports/(.+)/(.+)$', views_bitbucket.reports, name='manage'),
    # url(r'^linechart/$', views_bitbucket.line_chart),

    # Ajax Request URLs
    url(r'^subscribe/$', views_bitbucket.subscribe_repository),
    url(r'^unsubscribe/$', views_bitbucket.unsubscribe_repository),
    url(r'^unsubscribe-all/$', views_bitbucket.unsubscribe_all, name='unsubscribe-all'),
    url(r'^fetch-more-issues/$', views_bitbucket.fetch_more_issues),

    # Social Auth URLs
    url(r'', include('social.apps.django_app.urls', namespace='social'))

    # Admin URL
    # url(r'^admin/', include(admin.site.urls)),

)
