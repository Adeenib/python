from typing import Counter
from django.urls import path
from . import views
urlpatterns = [
    path('', views.counter),
    path('destroy_session', views.dectroy),
    path('plus_two', views.plus_two),
    path('plus_value', views.plus_value)

]
