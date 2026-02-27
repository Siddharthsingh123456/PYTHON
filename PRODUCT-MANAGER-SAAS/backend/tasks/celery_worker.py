from celery import Celery

from config import Config


celery_app = Celery('product_manager')
celery_app.conf.broker_url = Config.REDIS_URL
celery_app.conf.result_backend = Config.REDIS_URL


@celery_app.task
def ping():
    return 'pong'
