import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import os
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
def infoAboutCollection(request):
    if request.method=='POST':
        user = Account.objects.get(username=request.user.username)
        c = Collection.objects.filter(user=user,name_collection=request.POST['oldName'])
        mimetype = 'application/javascript'
        data = serializers.serialize('json', c)
        return HttpResponse(data,mimetype)
    return HttpResponse("Error/ No get")

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

import smtplib

@user_passes_test(isAuth,login_url="/accounts/login/")
def deleteRSS(request):
    if (request.POST.get("URL") is None) or (request.POST.get('nameCollection') is None):
        return HttpResponse("error");
    user = Account.objects.get(username=request.user.username)
    collection = Collection.objects.get(user=user,name_collection=request.POST['nameCollection'])
    rss = RSSFeed.objects.get(collection=collection,url=request.POST.get('URL'))
    if rss.collection.all().__len__()>1:
        rss.collection.remove(collection)
    else:
        rss.delete()
    return HttpResponse("Success")

@user_passes_test(isAuth,login_url="/accounts/login/")
def editCollection(request):
    if request.method=='POST':
        user = Account.objects.get(username = request.user.username)
        if Collection.objects.filter(user=user,name_collection = request.POST['newCollection']).__len__()>0 and request.POST['oldName']!=request.POST['newCollection']:
            return HttpResponse("Error/this name already exist")
        else:
            c = Collection.objects.get(user=user,name_collection=request.POST['oldName'])
            c.name_collection = request.POST['newCollection']
            c.format = request.POST['format']
            c.subject = request.POST['subject']
            # c.sendingTime = datetime.time(int(request.POST['sendingTime']))
            delta_sending_time = request.POST['delta_sending_time'];
            interval_sec = 0
            if "min" in delta_sending_time:
                interval_sec = int(delta_sending_time[:-3])*60
            elif "h" in delta_sending_time:
                interval_sec = int(delta_sending_time[:-1]) * 60 * 60
            else:
                interval_sec = int(delta_sending_time[:-1]) * 60 * 60 * 24
            c.delta_sending_time = interval_sec
            c.save()
            return HttpResponse("Success")
    else:
        return HttpResponse("Error/No get")


def send(request):
    send_mail1("cska631@gmail.com", "subj","text")
    return HttpResponse("asd")


def send_mail1( send_from, subject, text, files=["t.txt"],  port=587, isTls=True):
    password='Dodiplomanow!'
    server="smtp.gmail.com"
    msg = MIMEMultipart()
    recipients = ['vladimir.prikhodko@emc.com', 'cska631@gmail.com']

    msg['From'] = send_from
    msg['To'] = ", ".join(recipients)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if isTls: smtp.starttls()
    smtp.login("cska631@gmail.com",password)
    smtp.sendmail(send_from, recipients, msg.as_string())
    smtp.quit()