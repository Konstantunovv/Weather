import requests as rq
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    appid = '3304b6d5a429b079b8167ca7b5a5a190'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
    city = 'London'
    res = rq.get(url.format(city)).json()
    print(res)
    template = 'weather/home.html'
    return render(request,template)

# Create your views here.
