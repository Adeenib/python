from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'main.html', context)


def add_new(request):

    return render(request, 'addshow.html')


def read(request):
    # context = {
    #     'title': request.POST['title'],
    #     'network': request.POST['network'],
    #     'R_data': request.POST['R_data'],

    # }
    id = Addshow(request.POST)

    return redirect('shows/' + str(id))


def read_new(request, id):
    context = {"alaa": Show.objects.get(id=id)}
    return render(request, 'read.html', context=context)
