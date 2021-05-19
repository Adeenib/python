

from django import urls
from django.urls import path, include

urlpatterns = [
    path('', include('number.urls')),
]
