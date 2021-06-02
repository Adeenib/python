from django.urls import path
from . import views
urlpatterns = [
    path('', views.readall),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/', views.show_this),
    path('delete/<int:id>/', views.deleteshow),
    path('<int:id>/edit/', views.editshow),
    path('<int:id>/update/', views.update),



]
