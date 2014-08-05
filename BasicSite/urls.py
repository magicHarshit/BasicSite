from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BasicSite.views.home', name='home'),
    url(r'^', include('core.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^static', 'django.contrib.staticfiles.views.serve'),
)
