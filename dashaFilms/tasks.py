from celery import task
import celery
from celery.schedules import crontab
from celery.task import periodic_task
import datetime
from dashaFilms.models import Country

from django.core.mail import send_mail

@task()
def add(x, y):
    c = Country(name = "vova1")
    c.save()
    return x + y

