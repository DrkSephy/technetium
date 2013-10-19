from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'example.app.views.home'),
    url(r'^login/$', 'example.app.views.home'),
    url(r'^done/$', 'example.app.views.done', name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
    # Examples:
    # url(r'^$', 'technetium.views.home', name='home'),
    # url(r'^technetium/', include('technetium.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
