from django.shortcuts import render, HttpResponse, redirect
from .models import users


def index(request):
    context = {
        "all_the_users": users.objects.all()
    }
    return render(request, 'home.html', context)


def add_user(request):

    users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                         email_address=request.POST['email_address'], age=request.POST['age'])
    return redirect('/')


def get_firs_tname(request, id):
    i = {'user': users.objects.get(id=id)}
    return HttpResponse(f'{i['user']['first_name']}')
