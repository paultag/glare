from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'glare.views.home', name='home'),
    url(r'^profile/$', 'glare.views.profile', name='profile'),
)
