from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_user', views.add_user),
    path('getfirstname/<int:id>', views.get_firs_tname)
]
