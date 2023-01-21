from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    usd = 2.5
    return render(request, 'about.html', {'gretting':'USD', 'key2':usd})


def home(request):
    return HttpResponse('This is Home page')