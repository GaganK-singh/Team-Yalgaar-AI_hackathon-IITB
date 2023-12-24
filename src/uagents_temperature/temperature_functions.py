# src/uagents_temperature/temperature_functions.py
import requests

def fetch_current_temperature(location):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=YOUR_API_KEY')
        response.raise_for_status()
        temperature_kelvin = response.json()['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return temperature_celsius

    except requests.exceptions.RequestException as e:
        print(f"Error fetching temperature: {e}")
        return None
