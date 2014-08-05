from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^blog/$', 'core.views.blog', name='blog'),
    url(r'^contact/$', 'core.views.contact', name='contact'),
)
