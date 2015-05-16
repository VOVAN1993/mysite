from celery import task
import celery
import datetime
from novajoy.views import send_mail1


@celery.decorators.periodic_task(run_every=datetime.timedelta(seconds=20))
def my():
    send_mail1("cska631@gmail.com", "subj","text")