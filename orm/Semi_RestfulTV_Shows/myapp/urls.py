from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.add_new),
    path('add', views.read),
    path('shows/<int:id>', views.read_new),

]
