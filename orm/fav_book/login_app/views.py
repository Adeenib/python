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
        context = {'userfirstname': get_user(request.session['login']).first().first_name,
                   'userlastname': get_user(request.session['login']).first().last_name,
                   'userid': get_user(request.session['login']).first().id,
                   'allbooks': all_books()

                   }
        print(context['userfirstname'])
        return render(request, 'home.html', context)
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


def addbooktofav(request):
    if request.method == 'POST':
        userid = get_user(request.session['login']).first().id

        errors = create_book(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home/')
        elif len(errors) == 0:
            userid = get_user(request.session['login']).first().id

            context = add_book(request.POST, userid)

            add_book_to_fav(context['bookid'], userid)
            print(context['bookid'])
    return redirect('/home/')


def editbook(request, id):

    context = {
        'userfirstname': get_user(request.session['login']).first().first_name,
        'userlastname': get_user(request.session['login']).first().last_name,
        'userid': get_user(request.session['login']).first().id,
        'bookinfo': thebook(id),
        'userfav': user_fav_this_book(id)
    }
    return render(request, 'editbook.html', context)


def updatebook(request, id):
    if request.method == 'POST':
        userid = get_user(request.session['login']).first().id
        errors = create_book(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/edit/{id}/')
        update_book(id, userid, request.POST)
        return redirect('/home/')


def deletebook(request, id):
    delete_book(id)
    return redirect('/home/')


def unfav(request, id):
    userid = get_user(request.session['login']).first().id
    un_fav(userid, id)
    return redirect(f'/edit/{id}/')


def fav_it(request, id):
    userid = get_user(request.session['login']).first().id
    favit(userid, id)
    return redirect(f'/edit/{id}/')
