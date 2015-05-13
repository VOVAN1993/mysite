import json
import datetime
from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
import ast
from django.http import HttpResponse
from dashaFilms import viewsUtil
from dashaFilms.models import *
from dashaFilms.viewsUtil import *
import time


def aa(request):
    return HttpResponse("hello")

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

def getFilmByCountry(request, country):
    filtered = Film.objects.filter(country__name=country).exclude(poster_link__isnull=True)[:10]
    results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in filtered]
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

def addUser(request):
    if request.method != 'GET':
        return HttpResponse("fail")
    _name = request.GET.get("name")
    _age = request.GET.get("age")
    _sex =request.GET.get("sex")

    if(_name is None):
        return HttpResponse("name is empty")
    if MyUser.objects.filter(name=_name).count()>0 :
        return HttpResponse("User with this name exist")
    newUser = MyUser(name = _name, age = int(_age), sex = _sex)
    newUser.save()
    return HttpResponse("OK")

def addFriend(request):
    if request.method != 'GET':
        return HttpResponse("fail")

    userNameFrom = request.GET.get("userFrom")
    userNameTo = request.GET.get("userTo")
    if userNameFrom is None or userNameTo is None:
        return HttpResponse("fail")

    userFrom = MyUser.objects.filter(name=userNameFrom)
    userTo = MyUser.objects.filter(name=userNameTo)

    if len(userFrom)!=1 or len(userTo)!=1:
        return HttpResponse("fail")
    userFrom = userFrom[0]
    userTo = userTo[0]
    if userFrom.friends.filter(name=userNameTo).count() == 0:
        userFrom.friends.add(userTo)

    return HttpResponse("OK")

def getAllFriend(request):
    if request.method != 'GET':
        return HttpResponse("fail")
    userName = request.GET.get("user")
    if(userName is None):
        return HttpResponse("name is empty")
    if MyUser.objects.filter(name=userName).count()==0 :
        return HttpResponse("User with this username doesn't exist")
    user = MyUser.objects.get(name=userName)
    friends = user.friends.all()
    results = [ob.__str__() for ob in friends]
    return HttpResponse(json.dumps(results))

def getAllComments(request):
    if request.method != 'GET':
        return HttpResponse("fail")
    userName = request.GET.get("user")
    if(userName is None):
        return HttpResponse("name is empty")
    if MyUser.objects.filter(name=userName).count()==0 :
        return HttpResponse("User with this username doesn't exist")
    _user = MyUser.objects.get(name=userName)
    comm = Comment.objects.filter(user = _user)
    # results = [serializers.serialize('json', [ob, ], use_natural_keys=True) for ob in comm]

    results = [ob.as_json() for ob in comm]
    return HttpResponse(json.dumps(results))

def checkGET(request):
    if request.method != 'GET':
        return HttpResponse("fail")
    else: return True

def checkUser(request):
    userName = request.GET.get("user")
    if(userName is None):
        return HttpResponse("name is empty")
    if MyUser.objects.filter(name=userName).count()==0 :
        return HttpResponse("User with this username doesn't exist")
    return True

def checkFilm(request):
    film_id = request.GET.get("film")
    if film_id is None:
        return HttpResponse("film_id is empty")
    if Film.objects.filter(pk = film_id).count()==0 :
        return HttpResponse("Film with this id doesn't exist")
    return True

def checkComment(request):
    id = request.GET.get("comment")
    if(id is None):
        return HttpResponse("db doesnt have row with this pk")
    return True


def addComment(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    _film = viewsUtil.getFilm(request.GET.get("pk"))
    comm = Comment(user=_user,film = _film, comment = request.GET.get("comment"), timestamp = int(round(time.time() * 1000)))
    comm.save()
    return HttpResponse("OK")

def _likeComment(request, user):
    id_comment = request.GET.get("comment")
    filCom = user.likedComments.filter(pk=id_comment)
    if len(filCom) == 0:
        check_and_undislikeComment(user,id_comment)
        filCom = Comment.objects.get(pk=id_comment)
        filCom.like+=1
        filCom.save()
        user.likedComments.add(filCom)
        user.save()
        return HttpResponse("OK")
    elif len(filCom==1):
        return HttpResponse("This comment already liked")

def likeCommentReuest(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    ret = checkComment(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    _likeComment(request,_user)
    return HttpResponse("OK")

def _dislikeComment(request, user):
    id_comment = request.GET.get("comment")
    filCom = user.dislikedComments.filter(pk=id_comment)
    if len(filCom) == 0:
        check_and_unlikeComment(user, id_comment)
        filCom = Comment.objects.get(pk=id_comment)
        filCom.dislike+=1
        filCom.save()
        user.dislikedComments.add(filCom)
        user.save()
        return HttpResponse("OK")
    elif len(filCom==1):
        return HttpResponse("This comment already disliked")

def dislikeCommentReuest(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    ret = checkComment(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    _dislikeComment(request,_user)
    return HttpResponse("OK")

def getAllLikeComments(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    results = [ob.as_json() for ob in _user.likedComments.all()]
    return HttpResponse(json.dumps(results))

def getAllDisLikeComments(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    results = [ob.as_json() for ob in _user.dislikedComments.all()]
    return HttpResponse(json.dumps(results))

def getAllCommentsByFriends(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    friends = _user.friends.all()
    result = []
    for friend in friends:
        result.append([ob.as_json() for ob in friend.comment_set.all()])
    return HttpResponse(json.dumps(result))

def getAllRatingByFriends(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    friends = _user.friends.all()
    result = []
    for friend in friends:
        estimates = MyRating.objects.filter(user=friend)
        if len(estimates)==0:continue
        result.append([ob.as_json() for ob in estimates])
    return HttpResponse(json.dumps(result))

def setRatingRequest(request):
    ret = checkGET(request)
    if ret is not True:
        return ret
    ret = checkUser(request)
    if ret is not True:
        return ret
    ret = checkFilm(request)
    if ret is not True:
        return ret
    _user = MyUser.objects.get(name=request.GET.get("user"))
    _film = Film.objects.get(pk=request.GET.get("film"))
    _value = Value.objects.get(values=request.GET.get("value"))
    setRaiting(_user,_film,_value)
    return HttpResponse("OK")







