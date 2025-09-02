import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


def get_current_weather(city="Delhi"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

  

    return weather_data


if __name__ == "__main__":
    print(f"***Getting Weather Conditions***")

    city = input("Enter The City Name")
    if not bool (city.strip()):
        city="New Delhi"
    weather_data = get_current_weather()
    print("\n")
    pprint(weather_data)
