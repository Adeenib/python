from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create_book),
    path('books/<int:id>/', views.show_book),
    path('add_authers_to_book/', views.add_auther_to_book),
    path('authers/', views.show_all_authers),
    path('authers/create/', views.create_auther),
    path('authers/<int:id>/', views.show_auther),
    path('add_books_to_auther/', views.add_book_to_auther),



]
