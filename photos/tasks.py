from celery import shared_task
from django.core.management import call_command
from celery.utils.log import get_task_logger

from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)

@shared_task(name='task_save_latest_flickr_image')
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    save_latest_flickr_image()
    logger.info("Saved image from Flickr")