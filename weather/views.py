from django.shortcuts import render
import json
import urllib.request
from PIL import Image
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == 'POST':

        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                     city+'&units=metric&appid=7c0ed5d2ae36e6c46deccf9a52924547').read()
        json_data = json.loads(res)
        data = {
            "city": str(json_data['name']).upper(),
            "country_code": str(json_data['sys']['country']),
            "latitude": str(json_data['coord']['lat']),
            "longitude": str(json_data['coord']['lon']),
            "weather_main": str(json_data['weather'][0]['main']),
            "weather_desc": str(json_data['weather'][0]['description']),
            "weather_icon": str(json_data['weather'][0]['icon']),
            "temp": str(json_data['main']['temp']) + '°C',
            "feels_like": str(json_data['main']['feels_like']) + '°C',
            "mintemp": str(json_data['main']['temp_min']) + '°C',
            "maxtemp": str(json_data['main']['temp_max']) + '°C',
            "sunrise_local": datetime.utcfromtimestamp(int(json_data['sys']['sunrise']) + int(json_data['timezone'])).strftime('%H:%M:%S'),
            "sunset_local": datetime.utcfromtimestamp(int(json_data['sys']['sunset']) + int(json_data['timezone'])).strftime('%H:%M:%S'),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "visibility": str(json_data['visibility']),
            "wind_speed": str(json_data['wind']['speed']),
            "wind_deg": str(json_data['wind']['deg']),
            "clouds": str(json_data['clouds']['all']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
