import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "947fa8a19bb352dad98f82877607a41a"
    city = "Santiago"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"Temperature in {city}: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to get weather data")