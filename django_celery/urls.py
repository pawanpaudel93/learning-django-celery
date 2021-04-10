from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from feedback.views import FeedbackView
from photos.views import PhotoView
from news.views import NewsView

urlpatterns = [
    path('', PhotoView.as_view(), name="home"),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('news/', NewsView.as_view(), name='news'),
    path('admin/', admin.site.urls),
]
