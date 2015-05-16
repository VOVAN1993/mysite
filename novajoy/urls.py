from django.conf.urls import patterns, include, url
from novajoy import views

from django.contrib.auth import urls
from novajoy.views import viewCollection, addCollection

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.send, name='send'),

    url(r'^accounts/', include('registration.backends.default.urls')),


)