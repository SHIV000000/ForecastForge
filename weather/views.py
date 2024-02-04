# weather/views.py
import requests
import calendar
from datetime import datetime as dt
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from requests.exceptions import RequestException
from django.shortcuts import render
from credentials import API_KEY
import pytz
import logging

# Setup logging
logger = logging.getLogger(__name__)

# utc time now and later change it acc. to client's timezone
UTC = pytz.utc

def home(request):
    # RGB color for web app background
    rgb_night = [15, 32, 39, 44, 83, 100]
    rgb_sunny = [255, 102, 0, 204, 204, 0]
    rgb_body = [43, 50, 178, 20, 136, 204]

    geolocator = Nominatim(user_agent="weather_app")

    # if checks either form has been submitted or not
    # if yes searched is searched value
    # else searched is default value London, UK
    if request.POST.get('search') is not None:
        searched = request.POST.get('search')
    else:
        searched = "London, UK"

    location = geolocator.geocode(searched)
    if location is None:
        msg = f"Oops! {searched} not found. Please check the spelling and try again."
        context = {
            "message": msg,
            "rb": rgb_body,
        }
        return render(request, 'weather/main.html', context)

    # add your API key here
    api_key = API_KEY
    lat = location.latitude
    lon = location.longitude
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        # Add logging here to check the constructed URL
        logger.info(f"Requesting data from: {url}")

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # data is the JSON file
        data = response.json()

        # Convert timezone to string
        timezone = str(data["timezone"])

        today_time = pytz.timezone(timezone)
        local_time = dt.now(today_time)

        today_day_count = local_time.weekday()
        today_day_name = calendar.day_name[today_day_count]
        today_date_regular = local_time.strftime(' , %B %d')
        today_hour = int(local_time.strftime('%H'))
        # date variable outputs in format sunday, Nov 25
        date = today_day_name + today_date_regular

        address = searched

        current_temp = int(data["main"]["temp"])
        current_weather_desc = data["weather"][0]["description"]
        current_weather_desc_sml = data["weather"][0]["main"]
        # it displays moon and sun depending on it is either day or night
        is_it_night = (today_hour > 18 and today_hour <= 24) or (today_hour >= 0 and today_hour < 6)

        if is_it_night:
            rgb_body = rgb_night

        if current_weather_desc_sml == "Clear" and is_it_night:
            current_weather_desc_sml += "-night"

        if current_weather_desc_sml == "Clear" and not is_it_night:
            rgb_body = rgb_sunny

        current_weather_desc_small = 'static/icons/' + current_weather_desc_sml + '.svg'
        crnt_temp_high = int(data["main"]["temp_max"])
        crnt_temp_low = int(data["main"]["temp_min"])
        # api by default gives wind speed in m/s
        # to convert to miles per hr multiply by  2.237
        wind_speed = "{:.2f}".format((data["wind"]["speed"]) * 2.237)
        uv_index = 0  # Update this line with appropriate data from the response

        # 7 days weather forecast
        daily_weather = []  # Update this line with appropriate data from the response

        context = {
            'address': address,
            'date': date,
            'current_temp': current_temp,
            'current_weather_desc': current_weather_desc,
            'current_weather_desc_small': current_weather_desc_small,
            'crnt_temp_high': crnt_temp_high,
            'crnt_temp_low': crnt_temp_low,
            'wind_speed': wind_speed,
            'uv_index': uv_index,
            'daily_weather': daily_weather,
            'rb': rgb_body,
        }
        return render(request, 'weather/main.html', context)

    except (RequestException, GeocoderTimedOut, KeyError) as e:
        # Log the error for debugging purposes
        logger.error(f"Error: {e}")

        # Provide a user-friendly error message
        msg = f"Oops! An unexpected error occurred. Please try again later."
        context = {
            "message": msg,
            "rb": rgb_body,
        }
        return render(request, 'weather/main.html', context)
