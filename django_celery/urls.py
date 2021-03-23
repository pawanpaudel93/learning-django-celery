from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from feedback.views import FeedbackView
from photos.views import PhotoView

urlpatterns = [
    path('', PhotoView.as_view(), name="home"),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('admin/', admin.site.urls),
]
