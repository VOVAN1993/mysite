import datetime
import string
from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import feedparser

# Create your views here.
from django.template import loader, RequestContext
from novajoy.models import Account, Collection, RSSFeed


def isAuth(user):
    if user.username=="novajoyUser":
        return False
    return user.is_authenticated()

def isRss(RSSUrl):
    feed = feedparser.parse(RSSUrl)
    if feed['bozo']==1 :
        return False
    else:
        return True

@user_passes_test(isAuth,login_url="/accounts/login/")
def addCollection(request):
    #to write a decorator for definition ativete user
    if request.POST.get('newCollection') is None:
        return HttpResponse("Empty field newCollection")
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    user = Account.objects.get(username=request.user.username)
    if Collection.objects.filter(user=user,name_collection=request.POST['newCollection']).__len__()>0:
        response.write("The collection with such name already exists")
        return HttpResponse(response)
    delta_sending_time = request.POST['delta_sending_time'];
    interval_sec = 0
    if "min" in delta_sending_time:
        interval_sec = int(delta_sending_time[:str.find(delta_sending_time,"min")])*60
    elif "h" in delta_sending_time:
        interval_sec = int(delta_sending_time[:str.find(delta_sending_time,"h")]) * 60 * 60
    else:
        interval_sec = int(delta_sending_time[:str.find(delta_sending_time,"h")]) * 60 * 60 * 24

        # c = Collection(user=user,name_collection=request.POST['newCollection'],last_update_time=datetime.datetime.now(),
        # delta_sending_time=interval_sec,format = request.POST['format'],subject=request.POST['format'])
    c = Collection(user=user,name_collection=request.POST['newCollection'],last_update_time=datetime.datetime.now(),
                   delta_sending_time=interval_sec,format=request.POST['format'],subject=request.POST['subject'])
    c.save()

    response.write("Success")
    return HttpResponse(response)

@user_passes_test(isAuth,login_url="/accounts/login/")
def deleteCollection(request):
    if request.POST.get('nameCollection') is None:
        return HttpResponse("error")
    user = Account.objects.get(username=request.user.username)
    collection = Collection.objects.get(user=user,name_collection=request.POST['nameCollection'])
    rss = RSSFeed.objects.filter(collection=collection)
    #for _rss in rss:

    collection.delete()

    return HttpResponse("Success")

@user_passes_test(isAuth,login_url="/accounts/login/")
def viewCollection(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    try:
        user = Account.objects.get(username=request.user.username)
        collection = Collection.objects.filter(user=user)
        return render_to_response('mainPage.html',{'collection':collection,'user_name':user.username},context_instance=RequestContext(request))
    except Account.DoesNotExist:
        return HttpResponse("This User don't have collections")

@user_passes_test(isAuth,login_url="/accounts/login/")
def viewURL(request):
    if request.POST.get('nameCollection') is None:
        return HttpResponse("Empty nameCollection")
    user = Account.objects.get(username=request.user.username)
    collection = Collection.objects.get(user=user,name_collection=request.POST['nameCollection'])
    rss = RSSFeed.objects.filter(collection=collection)
    mimetype = 'application/javascript'
    data = serializers.serialize('json', rss)
    return HttpResponse(data,mimetype)

@user_passes_test(isAuth,login_url="/accounts/login/")
def addRSS(request):
    if request.POST.get('nameOfNewRSS') is None:
        return HttpResponse("Empty field nameOfNewRSS")
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    if isRss(request.POST.get('nameOfNewRSS'))==True:
        user = Account.objects.get(username=request.user.username)
        collection = Collection.objects.get(user=user,name_collection=request.POST['nameCollection'])
        if RSSFeed.objects.filter(collection=collection,url=request.POST.get('nameOfNewRSS')).__len__()>0:
            response.write("The RSS with such url already exists")
            return HttpResponse(response)
        if RSSFeed.objects.filter(url=request.POST.get('nameOfNewRSS')).__len__()>0:
            rss = RSSFeed.objects.get(url=request.POST.get('nameOfNewRSS'))
            rss.collection.add(collection)
            rss.save()
            return HttpResponse("Success")
        else:
            t = datetime.datetime.now()
            newRSS = RSSFeed(url=request.POST.get('nameOfNewRSS'),pubDate=t.strftime("%Y-%m-%d %H:%M:%S"),spoiled=False)
            newRSS.save()
            newRSS.collection.add(collection)
            newRSS.save()
            response.write("Success")
            return HttpResponse(response)
    else:
        response.write("This address doesn't belong to RSS")
        return HttpResponse(response)

def hello(request):
    return HttpResponse("asd")