import requests
from django.shortcuts import render
from .models import City
from .forms import Cityform
def index(request):
    url = 'http://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    
    if request.method == 'POST':
        form = Cityform(request.POST)
        form.save()

    form = Cityform()

    cities = City.objects.all() 

    weather_data = []
    for city in cities:
         r = requests.get(url.format(city)).json()

         city_weather = {
            'city' :  city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
             }

         weather_data.append(city_weather)

    context = {'weather_data':weather_data, 'form':form } 
    print(weather_data)
    return render(request,'weatherapp/weather.html',context)

