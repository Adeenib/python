from django.http import request
from django.shortcuts import render, HttpResponse


def login(request):
    return render(request, "login.html")
# if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	val_from_field_two = request.POST["two"]


def info(request):

    form = {
        'name': request.POST['name'],
        'loc': request.POST['loc'],
        'lang': request.POST['lang'],
        'comment': request.POST['comment']
    }

    return render(request, 'result.html', form)
