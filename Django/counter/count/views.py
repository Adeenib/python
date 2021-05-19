from django.shortcuts import render, HttpResponse, redirect


def counter(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    elif 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    if 'realcount' not in request.session:
        request.session['realcount'] = 1
    elif 'realcount' in request.session:
        request.session['realcount'] = request.session['realcount'] + 1

    return render(request, 'count.html')


def dectroy(request):
    request.session['count'] = 0
    request.session['realcount'] = request.session['realcount'] - 1
    return redirect("/")


def plus_two(request):
    request.session['count'] = request.session['count'] + 1
    request.session['realcount'] = request.session['realcount'] - 1
    return redirect("/")


def plus_value(request):
    value = request.POST['value']
    if value == 'zero':
        request.session['realcount'] = request.session['realcount'] - 1
        request.session['count'] = request.session['count'] - 1
        return redirect("/")
    else:
        value = int(request.POST['value'])-1
        request.session['count'] = request.session['count'] + value
        return redirect("/")
