from django.shortcuts import render, redirect

import random


def home(request):
    if "number" not in request.session:
        request.session['number'] = random.randint(1, 100)

    return render(request, 'home.html')


def test(request):

    num = int(request.POST['value'])
    if int(num) > request.session['number']:
        request.session['test'] = 'high'
    elif int(num) < request.session['number']:
        request.session['test'] = 'low'
    elif int(num) == request.session['number']:
        return redirect('/congrats')
    return redirect('/')


def congrats(request):
    request.session['congrats'] = request.session['number']
    del request.session['number']
    del request.session['test']
    return render(request, 'congrats.html')
