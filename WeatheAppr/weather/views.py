import requests as rq

from django.shortcuts import render

from .forms import CityForm
from .models import City


def index(request):
    appid = '3304b6d5a429b079b8167ca7b5a5a190'
    url = (
        'https://api.openweathermap.org/data/2.5/weather?q={'
        '}&units=metric&appid=' + appid
    )
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = rq.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    template = 'weather/home.html'
    return render(request, template, context)


# Create your views here.
