from django.conf.urls import patterns, include, url
from django.contrib import admin
from novajoy.views import hello
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^novajoy/', include('novajoy.urls')),
)
