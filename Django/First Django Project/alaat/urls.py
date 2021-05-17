from django.urls import path, include

urlpatterns = [
    path('', include('firstapp.urls')),
    path('blogs/', include('firstapp.urls')),

]
