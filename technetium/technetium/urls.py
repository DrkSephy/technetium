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
    url(r'^dashboard/$', views_bitbucket.dashboard, name='dashboard'),
    url(r'^issues/$', views_bitbucket.dashboard_issues, name='issues'),
    url(r'^linechart/$', views_bitbucket.line_chart),
    url(r'^piechart/$', views_bitbucket.pie_chart),
    url(r'^manage/$', views_bitbucket.manage_repositories, name='manage'),

    # Ajax Request URLs
    url(r'^subscribe/$', views_bitbucket.subscribe_repository),
    url(r'^unsubscribe/$', views_bitbucket.unsubscribe_repository),
    url(r'^unsubscribe-all/$', views_bitbucket.unsubscribe_all_repository),

    # Social Auth URLs
    url(r'', include('social.apps.django_app.urls', namespace='social'))

    # Admin URL
    # url(r'^admin/', include(admin.site.urls)),

)
