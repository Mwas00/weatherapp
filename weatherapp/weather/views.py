import requests
from django.shortcuts import render

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = ''
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        data = response.json()
        
        if data.get('cod') != 200:
            error_message = "City not found. Please try again."
            return render(request, 'weather/weather.html', {'error': error_message})
        
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
        }

        return render(request, 'weather/weather.html', {'weather': weather_data})
    
    return render(request, 'weather/weather.html')
