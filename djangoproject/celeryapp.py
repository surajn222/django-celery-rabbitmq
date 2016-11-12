from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('djangoproject',
             broker='amqp://admin:password@vagrant-ubuntu-trusty-64/vhost',
             backend='amqp://',
             include=['djangoproject.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
