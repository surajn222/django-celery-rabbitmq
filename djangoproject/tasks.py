from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

#app = Celery('djangoproject')

app = Celery('djangoproject', backend='amqp://', broker = 'amqp://admin:password@vagrant-ubuntu-trusty-64/vhost')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#from __future__ import absolute_import, unicode_literals
#from .celeryapp import app
#from celery import task

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def email():
    import smtplib
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("surajn222@gmail.com", "surajn222@")
 
    msg = "YOUR MESSAGE!"
    server.sendmail("surajn222@gmail.com", "surajn222@gmail.com", msg)
    server.quit()
    return 2
