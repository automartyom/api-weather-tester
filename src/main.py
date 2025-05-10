import os
from dotenv import load_dotenv
load_dotenv()
import requests

def get_weather(city):
    api_key = os.environ.get("WEATHER_API_KEY")
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
    return response