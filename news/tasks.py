from celery import shared_task
from django.core.management import call_command
from celery.utils.log import get_task_logger

from news.utils import save_top_news

logger = get_task_logger(__name__)

@shared_task(name='task_save_top_news')
def task_save_top_news():
    """
    Saves top news from newsapi
    """
    save_top_news()
    logger.info("Saved news from newsapi")