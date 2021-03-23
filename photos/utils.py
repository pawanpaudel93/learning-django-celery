import json
import requests

from photos.models import Photo

FLICKR_JSON_FEED_URL = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1"

def get_latest_flickr_image():
    """
    Grabs the latest image from the flick public image feed
    """
    feed = requests.get(FLICKR_JSON_FEED_URL).json()
    images = feed['items']
    return images[0]


def save_latest_flickr_image():
    """
    We get the lastest image and save it to our Photo Model in the Database
    """
    flickr_image = get_latest_flickr_image()
    # lets make sure we don't save the same image more than once
    # we are assuming each Flickr image has a unique Link
    if not Photo.objects.filter(link=flickr_image['link']).exists():
        photo = Photo(
            title=flickr_image['title'],
            link=flickr_image['link'],
            image_url=flickr_image['media']['m'],
            description=flickr_image['description']
        )
        photo.save()
