from django.db.models.fields import DateField
from django.shortcuts import redirect, render
from tv_app.models import *
from time import strftime
from django.contrib import messages


def readall(request):
    context = {
        'shows': readshows(),
    }

    return render(request, 'read_all.html', context)


def new(request):

    return render(request, 'addshow.html')


def create(request):
    data = request.POST
    errors = Shows.objects.basic_validator(data)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new/')

    new_show = createshow(data)
    return redirect('/shows/'+str(new_show.id))


def show_this(request, id):

    context = {'show_data': showthis(id)
               }
    return render(request, 'show_this.html', context)


def deleteshow(request, id):
    delete(id)
    return redirect('/shows')


def editshow(request, id):
    time = showthis(id).release
    context = {
        'data': showthis(id),
        'time': time.strftime('%Y-%m-%d')
    }
    return render(request, 'Edit.html', context)


def update(request, id):

    data = request.POST
    errors = Shows.objects.basic_validator(data)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')

    data = updateshow(request.POST)
    return redirect('/shows/'+str(id))
