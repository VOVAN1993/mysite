from django.conf.urls import patterns, include, url
from django.contrib import admin
from novajoy.my import RegBackend
from novajoy.views import *

urlpatterns = patterns('',
    url(r'^dasha/', include('dashaFilms.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^novajoy/', include('novajoy.urls')),
    url(r'^send/', send),
    url(r'^$',viewCollection),
    url(r'^addCollection/$',addCollection),
    url(r'^deleteCollection/$',deleteCollection),
    url(r'^addRSS/$',addRSS),
    url(r'^$',viewCollection),
    url(r'^selectURL/$',viewURL),
    url(r'^deleteRSS/$',deleteRSS),
    url(r'^editCollection/$',editCollection),
    url(r'^infoAboutCollection/$',infoAboutCollection),
    url(r'^selectURL/$',viewURL),

    url(r'^accounts/register/$',
                           RegBackend.as_view(),
                           name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),




                       # url(r'^captcha/', include('captcha.urls')),
                       # url(r'^$',viewCollection),
                       # url(r'^accounts/passwordReset/$',resetPassword),
                       # url(r'^accounts/passwordReset/confirm/(?P<activation_key>\w+)/$',resetPasswordConfirm),
                       # url(r'^accounts/', include('backends.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       # url(r'^about/',about),
                       # url(r'^contact/',contact),
                       # url(r'^changedPassword/',changedPassword),
)
