
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import models


def index(request):
    context = {
        'all_dojo': models.Dojo.objects.all(),
        'all_ninja': models.Ninja.objects.all()
    }
    return render(request, 'home.html', context)


def create(request):
    if request.POST['forms'] == 'dojo':
        models.create(request.POST)
    elif request.POST['forms'] == 'ninja':
        models.create_ninja(request.POST)

    return redirect('/')
