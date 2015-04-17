import json
from django.core import serializers
import ast
from django.http import HttpResponse
from dashaFilms.models import *
from dashaFilms.viewsUtil import *


def aa(request):
    return HttpResponse("hello")


def parse(request):
    with open("./round2/norm1.txt") as f:
        contents = f.readlines()
    arr = []
    for line in contents:
        dict = ast.literal_eval(line)
        genres = dict['Genre'].split(",")
        directors = dict['Director'].split(",")
        actors = dict['Actors'].split(",")
        countries = dict['Country'].split(",")
        dbGenres = getGenres(genres)
        dbActors = getActors(actors)
        dbDirectors = getDirectors(directors)
        dbCountries = getCountries(countries)
        dbName = dict['Title']
        dbName_rus = None if dict['rus_name'] == '' else dict['rus_name']
        dbTitle = None if dict['Plot'] == ''else dict['Plot']
        dbImdbID = None if dict['imdbID'] == '' or dict['imdbID'] == 'N/A' else dict['imdbID']
        dbTitle_rus = None if dict['rus_title'] == '' else dict['rus_title']
        dbTime = None if dict['Runtime'] == '' else dict['Runtime']
        dbYear = None if dict['Year'] == '' else dict['Year']
        dbPoster_link = None if dict['Poster'] == '' else dict['Poster']
        dbImbdRating = None if dict['imdbRating'] == '' or dict['imdbRating'] == 'N/A' else dict['imdbRating']

        createFilm(dbName, dbName_rus, dbTitle, dbTitle_rus, dbTime, dbYear, dbImbdRating, dbImdbID, dbPoster_link,
                   dbGenres, dbActors,
                   dbDirectors, dbCountries)
        arr.append(dbName)
        print(dbName)

    return HttpResponse(arr)


def getFilm(request, name):
    try:
        film = Film.objects.get(name=name)
        st = serializers.serialize('json', [film, ], use_natural_keys=True)
        return HttpResponse(st)
    except Film.DoesNotExist:
        return HttpResponse("{response:False}")


def getFilmByRusName(request, rus_name):
    filtered = Film.objects.filter(name_rus=rus_name)
    results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in filtered]
    # ret = json.dumps(results).__str__()
    return HttpResponse(results)


def getFilmsByActor(request, actor_name):
    try:
        actor = Actor.objects.get(name=actor_name)
        films = actor.film_set.all()
        results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in films]
        return HttpResponse(results)
    except Actor.DoesNotExist:
        return HttpResponse("{response:False}")

def getFilmsByDirector(request, director_name):
    try:
        director = Director.objects.get(name=director_name)
        films = director.film_set.all()
        results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in films]
        return HttpResponse(results)
    except Actor.DoesNotExist:
        return HttpResponse("{response:False}")


def getFilmsByCountry(request, country_name):
    try:
        country = Country.objects.get(name=country_name)
        films = country.film_set.all()
        results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in films]
        return HttpResponse(results)
    except Actor.DoesNotExist:
        return HttpResponse("{response:False}")

def getFilmsByYear(request, year):
    try:
        films = Film.objects.filter(year = int(year))
        results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in films]
        return HttpResponse(results)
    except Actor.DoesNotExist:
        return HttpResponse("{response:False}")


