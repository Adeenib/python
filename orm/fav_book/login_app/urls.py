from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_reg),
    path('home/', views.home),
    path('login_registration/', views.check),
    path('logout/', views.logout),
    path('add_booktofav/', views.addbooktofav),
    path('unfav/<int:id>/', views.unfav),
    path('fav_it/<int:id>/', views.fav_it),
    path('edit/<int:id>/', views.editbook),
    path('update/<int:id>/', views.updatebook),
    path('delete/<int:id>/', views.deletebook),


]
