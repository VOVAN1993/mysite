import datetime
import string
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import feedparser

# Create your views here.
from django.template import loader, RequestContext
from novajoy.models import Account, Collection


def isAuth(user):
    if user.username=="novajoyUser":
        return False
    return user.is_authenticated()

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
def viewCollection(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    try:
        user = Account.objects.get(username=request.user.username)
        collection = Collection.objects.filter(user=user)
        return render_to_response('mainPage.html',{'collection':collection,'user_name':user.username},context_instance=RequestContext(request))
    except Account.DoesNotExist:
        return HttpResponse("This User don't have collections")

def hello(request):
    return HttpResponse("asd")