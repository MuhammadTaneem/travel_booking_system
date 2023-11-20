from django.template.defaulttags import url
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
]