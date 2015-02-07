from django.conf.urls import patterns, include, url
from novajoy import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.hello, name='hello'),
    url(r'^accounts/', include('registration.backends.default.urls')),


)