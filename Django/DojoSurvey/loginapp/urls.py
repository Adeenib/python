from django.urls import path
from django.urls import path
from . import views
urlpatterns = {
    path('', views.login),
    path('result', views.info),
}
