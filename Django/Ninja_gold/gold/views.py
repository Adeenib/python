from django.shortcuts import redirect, render
import random


def home(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    elif 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'home.html')


def process_money(request):
    if request.method == "POST":
        gold = 0
        if request.POST['action'] == 'farm':
            gold = random.randint(10, 20)
            request.session['activities'].append(
                'You are earned ' + str(gold) + " golds")

        elif request.POST['action'] == 'Cave':
            gold = random.randint(5, 10)
            request.session['activities'].append(
                'You are earned ' + str(gold) + " golds")

        elif request.POST['action'] == 'House':
            gold = random.randint(2, 5)
            request.session['activities'].append(
                'You are earned ' + str(gold) + " golds")

        elif request.POST['action'] == 'Casino':
            gold = random.randint(-50, 50)
            if gold > 0:
                request.session['activities'].append(
                    'You are earned ' + str(gold) + " golds")
            elif gold < 0:
                request.session['activities'].append(
                    'You are lose ' + str(abs(gold)) + " golds")
    request.session['gold'] += gold
    return redirect('/')
