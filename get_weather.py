#get_weather.py

import requests
import os
from dotenv import load_dotenv

#Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    #1. Create the APIC endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    #2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" #temperature in Celsius
    }

    #3. Make the request
    response = requests.get(url, params=params)

    #4. Parse JSON
    data = response.json()

    #5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    #6. Print
    print(f"In {city_name}, it is {temp} degrees celsius with {humidity}% humidity and {description}.")

def get_city():
    return input("Enter a city to get its weather: ")

if __name__ == "__main__":
    city = get_city()
    get_weather(city)