from dashaFilms.models import *
import time


def getGenres(names):
    returnGenres = []
    for genre in names:
        genre = genre.strip()
        if genre == 'N/A': continue
        if len(Genre.objects.filter(name=genre)) == 0:
            dbGenre = Genre(name=genre)
            dbGenre.save()
            returnGenres.append(dbGenre)
        else:
            returnGenres.append(Genre.objects.get(name=genre))
    return returnGenres


def getActors(actors):
    returnActors = []
    for actor in actors:
        actor = actor.strip()
        if actor == 'N/A': continue
        if len(Actor.objects.filter(name=actor)) == 0:
            dbActor = Actor(name=actor)
            dbActor.save()
            returnActors.append(dbActor)
        else:
            returnActors.append(Actor.objects.get(name=actor))
    return returnActors


def getDirectors(directors):
    returnDirectors = []
    for director in directors:
        director = director.strip()
        if director == 'N/A': continue
        if len(Director.objects.filter(name=director)) == 0:
            dbDirector = Director(name=director)
            dbDirector.save()
            returnDirectors.append(dbDirector)
        else:
            returnDirectors.append(Director.objects.get(name=director))
    return returnDirectors


def getCountries(countries):
    returnCountries = []
    for country in countries:
        country = country.strip()
        if country == 'N/A': continue
        if len(Country.objects.filter(name=country)) == 0:
            dbCountry = Country(name=country)
            dbCountry.save()
            returnCountries.append(dbCountry)
        else:
            returnCountries.append(Country.objects.get(name=country))
    return returnCountries

def getFilmByPK(_pk):
    try:
        return Film.objects.get(pk = _pk)
    except Film.DoesNotExist:
        return None
def createFilm(dbName, dbName_rus, dbTitle, dbTitle_rus, dbTime, dbYear, dbImbdRating, dbImbdID, dbPoster, dbGenres, dbActors, dbDirectors,
               dbCountries):
    if len(Film.objects.filter(name = dbName, imbdID = dbImbdID)) != 0 :
        return Film.objects.get(name = dbName, imbdID = dbImbdID)
    film = Film(name=dbName, name_rus=dbName_rus, title=dbTitle, title_rus=dbTitle_rus, time=dbTime, poster_link = dbPoster, imbdID = dbImbdID, year=dbYear,
                imbdRating=dbImbdRating)
    film.save()
    for genre in dbGenres:
        film.genres.add(genre)
    film.save()
    for actor in dbActors:
        film.actors.add(actor)
    film.save()
    for director in dbDirectors:
        film.directors.add(director)
    film.save()
    for country in dbCountries:
        film.country.add(country)
    film.save()

def check_and_unlikeComment(user, _pk):
    if len(user.likedComments.filter(pk=_pk))>0:
        com = user.likedComments.get(pk=_pk)
        com.like-=1
        com.save()
        user.likedComments.remove(com)
        user.save()

def check_and_undislikeComment(user, _pk):
    if len(user.dislikedComments.filter(pk=_pk))>0:
        com = user.dislikedComments.get(pk=_pk)
        com.dislike-=1
        com.save()
        user.dislikedComments.remove(com)
        user.save()

def setRaiting(_user,_film,_value):
    ratings = MyRating.objects.filter(user = _user)
    for rating in ratings:
        if rating.film.pk == _film.pk :
            rating.delete()
            summ = _film.estim_num*_film.estim_mid
            _film.estim_num-=1
            if _film.estim_num == 0 :
                _film.estim_mid = 0
            else:
                _film.estim_mid= (summ-int(rating.value.values))/_film.estim_num
            break

    r = MyRating(value = _value, user = _user, film = _film, timestamp = int(round(time.time() * 1000)))
    r.save()

    summ = _film.estim_mid*_film.estim_num
    _film.estim_num+=1
    _film.estim_mid = (summ+int(_value.values))/_film.estim_num

    _film.save()