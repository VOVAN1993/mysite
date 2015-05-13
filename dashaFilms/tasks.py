from celery import task
import celery
from celery.schedules import crontab
from celery.task import periodic_task
import datetime
from dashaFilms.models import Country


@task()
def add(x, y):
    c = Country(name = "vova1")
    c.save()
    return x + y

@celery.decorators.periodic_task(run_every=datetime.timedelta(seconds=5))
def my():
    print("vova")