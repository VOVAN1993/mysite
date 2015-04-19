from django.conf.urls import patterns, include, url
from dashaFilms.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/$', parse),
    url(r'^parseGenre/$', parseGenre),
    url(r'^parseCountry/$', parseCountry),
    url(r'^getFilmByCountry/(?P<country>[\w|\W]+)$', getFilmByCountry),
    url(r'^getFilm/(?P<name>[\w|\W]+)$', getFilm),
    url(r'^getFilmByRusName/(?P<rus_name>[\w|\W]+)$', getFilmByRusName),
    url(r'^getFilmByActor/(?P<actor_name>[\w|\W]+)$', getFilmsByActor),
    url(r'^getFilmByDirector/(?P<director_name>[\w|\W]+)$', getFilmsByDirector),
    url(r'^getFilmByCountry/(?P<country_name>[\w|\W]+)$', getFilmsByCountry),
    url(r'^getFilmByYear/(?P<year>\d+)$', getFilmsByYear),



)