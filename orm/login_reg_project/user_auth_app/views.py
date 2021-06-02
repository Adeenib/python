from django.shortcuts import render, redirect, HttpResponse
from user_auth_app.models import *


def home(request):
    if 'user' in request.session:
        return redirect('/welcome')
    return render(request, 'home.html')
# Create your views here.


def login(request):
    useremail = request.POST['email']
    password = request.POST['password']

    users = User.objects.filter(email=useremail)

    if len(users) == 0:
        return redirect('/')

    user = users.first()
    if user.password != password:
        return redirect('/')
    data = {
        'username': user.username,
        'password': user.password,
        'address': user.address,
        'useremail': user.email

    }

    request.session['user'] = data
    return redirect('/welcome')


def register(request):
    username = request.POST['name']
    password = request.POST['password']
    address = request.POST['address']
    useremail = request.POST['email']
    data = {
        'username': username,
        'password': password,
        'address': address,
        'useremail': useremail

    }

    user = User.objects.create(username=username, password=password,
                               address=address,
                               email=useremail)
    request.session['user'] = data
    return redirect('/welcome')


def welcome(request):
    if 'user' in request.session:
        user = request.session['user']
    return render(request, 'welcome.html', user)


def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')
