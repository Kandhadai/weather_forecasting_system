# boundaries/weather_data_boundary.py

from HU.Project.Website.controls.weather_control import WeatherControl
from flask import request


class WeatherBoundary:
    def get_latest_weather(self, request):
        """
        Passes the location to the control object to fetch the latest weather.
        """
        control = WeatherControl()
        location = request.form.get('location')

        if location:
            # Pass the location to the control to fetch the weather data
            weather_data = control.get_latest_weather(location)
            return weather_data, location
        else:
            return None, None

