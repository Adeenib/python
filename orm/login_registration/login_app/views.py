from django.shortcuts import render, redirect
from .models import *
from django.http import request
from django.contrib import messages


def log_reg(request):
    if 'login' in request.session:
        print(request.session['login'])
        return redirect('/home/')
    return render(request, 'log_reg.html')


def logout(request):
    if 'login' in request.session:
        request.session.clear()
    return redirect('/')


def home(request):
    if 'login' in request.session:
        print(request.session['login'])
        return redirect('/wall/')
    return redirect('/')


def check(request):
    if request.method == 'POST':
        data = request.POST
        if data['log_reg'] == 'register':
            errors = create_user(data)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            request.session['login'] = data['email']
            return redirect('/home')

        elif data['log_reg'] == 'login':
            loginerrors = login_user(data)
            print(loginerrors)
            print('#'*30)
            if 'login' in loginerrors:
                return redirect('/')
            elif 'login' not in loginerrors:
                request.session['login'] = data['email']
                return redirect('/home')

    return redirect('/')


def wall(request):
    allposts = {'posts': all_post(),
                'comment': all_com_of_post()
                }
    print(allposts)
    print('alaa'*330)

    return render(request, 'wall.html', allposts)


def walltest(request):
    if 'login' in request.session:
        return redirect('/')
        #allpostcomments = all_postcomment(userdata)

    return redirect('/')


def addpost(request):
    if request.method == 'POST':
        if 'login' in request.session:
            userdata = get_user(request.session['login']).email
            print(userdata)
            print(userdata)
            print(userdata)
            add_post(request.POST['post'], userdata)
            return redirect('/wall/')
    return redirect('/')


def addcom(request):
    if request.method == 'POST':
        userdata = get_user(request.session['login']).email
        print(userdata)

        add_com(request.POST, userdata)
        return redirect('/wall/')


def delete(request, id):
    delete_com(id)
    return redirect('/wall/')
