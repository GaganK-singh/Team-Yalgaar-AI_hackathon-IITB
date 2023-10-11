from uagents import Agent, Bureau
import requests
from sklearn.linear_model import LinearRegression
import numpy as np

agent1 = Agent(name="name1", seed="name1 recovery phrase")
agent2 = Agent(name="name2", seed="name2 recovery phrase")

@agent1.on_interval(period=3.0)
async def get_real_time_weather(api_key, location):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": location,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature_celsius = data["current"]["temperature"]
        weather_description = data["current"]["weather_descriptions"][0]
        return temperature_celsius, weather_description
    else:
        print("Failed to fetch weather data.")
        return None

if __name__ == "__main__":
    api_key = "YOUR_APIKEY"  #Define your apikey in .env file
    location = input(str(""))  

    weather_data = get_real_time_weather(api_key, location)

    if weather_data is not None:
        temperature, description = weather_data
        print(f"The current temperature in {location} is {temperature}°C, and the weather is {description}.")
        min_temperature = 10.0
        max_temperature = 30.0
        toaster = ToastNotifier()
        print(min_temperature)
        print(temperature)

        
        if temperature > min_temperature:
            print(f"Temperature in {location} is below the minimum threshold of {min_temperature}°C.")
            toaster.show_toast("Temperature Alert", f"Temperature in {location} is below the minimum threshold of {min_temperature}°C.", duration=5)
        elif temperature < max_temperature:
            print(f"Temperature in {location} is above the maximum threshold of {max_temperature}°C.")
            toaster.show_toast("Temperature Alert", f"Temperature in {location} is above the maximum threshold of {max_temperature}°C.", duration=5)
        else:
            print("not working")


@agent2.on_interval(period=3.0)
def run_temperature_alert_agent(api_key, location):
    agent = TemperatureAlertAgent(api_key, location)
    agent.run()