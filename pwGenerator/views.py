from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'pwGenerator/home.html')


def generatePassword(options):
    print('options is what man?', options)
    characters = list('abcdefghijklmnopqrstuvwxyz')

    genPassword = ''

    if options['uppercase']:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if options['special']:
        characters.extend(list('!@#$%^&*()_+'))

    if options['numbers']:
        characters.extend(list('0123456789'))

    length = options['length']

    for x in range(length):
        genPassword += random.choice(characters)

    return genPassword


def password(request):
    # Options
    length = int(request.GET.get('pass-length', 8))
    upper = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    options = {'length': length, 'uppercase': upper,
               'special': special, 'numbers': numbers}

    genPassword = generatePassword(options)

    return render(request, 'pwGenerator/password.html', {'password': genPassword})


def about(request):
    return render(request, 'pwGenerator/about.html', {'name': 'NoerGitKat'})
