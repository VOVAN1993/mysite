from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext


def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
