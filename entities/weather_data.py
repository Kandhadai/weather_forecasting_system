from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, date

# Use TYPE_CHECKING to prevent runtime circular imports
from HU.Project.Website.dao.weather_dao import WeatherDataDAO


class WeatherData:
    def __init__(self, location, temperature, conditions, humidity, wind_speed, date):
        self.location = location
        self.temperature = temperature
        self.conditions = conditions
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.date = date

    @staticmethod
    def get_latest_weather(location):
        """Fetches the latest weather data for the specified location from the database."""
        weather_data = WeatherDataDAO.fetch_latest_weather(location)
        if weather_data:
            return WeatherData(
                    location=weather_data[0],  # Assuming location is the first field in the result
                    temperature=weather_data[1],  # Assuming temperature is the second field
                    conditions=weather_data[2],  # Assuming conditions is the third field
                    humidity=weather_data[3],  # Assuming humidity is the fourth field
                    wind_speed=weather_data[4],  # Assuming wind speed is the fifth field
                    date=weather_data[5]  # Assuming date is the sixth field
                )
        return None

    @staticmethod
    def get_today_forecast(location):
        """Fetches today's forecast for the specified location."""
        forecast_data = WeatherDataDAO.fetch_today_forecast(location)
        if forecast_data:
            return WeatherData(location=forecast_data['location'], temperature=forecast_data['temperature'],
                               conditions=forecast_data['conditions'], humidity=forecast_data['humidity'],
                               wind_speed=forecast_data['wind_speed'], date=forecast_data['date'])
        return None

    @staticmethod
    def get_extended_forecast(location, days):
        """Fetches the extended forecast for a given number of days."""
        result = WeatherDataDAO.fetch_extended_forecast(location, days)

        forecast_list = []
        for data in result:
            # Assuming result is a tuple, and you need to access fields by index
            forecast_list.append(
                WeatherData(
                    location=data[0],  # Assuming location is the first field in the result
                    temperature=data[1],  # Assuming temperature is the second field
                    conditions=data[2],  # Assuming conditions is the third field
                    humidity=data[3],  # Assuming humidity is the fourth field
                    wind_speed=data[4],  # Assuming wind speed is the fifth field
                    date=data[5]  # Assuming date is the sixth field
                )
            )
        return forecast_list

    @staticmethod
    def get_historical_data(location, start_date, end_date):
        """Fetches historical weather data for a specified location and date range."""
        historical_data = WeatherDataDAO.fetch_historical_data(location, start_date, end_date)
        historical_list = []
        for data in historical_data:
            historical_list.append(
                WeatherData(
                    location=data[0],  # Assuming location is the first field in the result
                    temperature=data[1],  # Assuming temperature is the second field
                    conditions=data[2],  # Assuming conditions is the third field
                    humidity=data[3],  # Assuming humidity is the fourth field
                    wind_speed=data[4],  # Assuming wind speed is the fifth field
                    date=data[5]  # Assuming date is the sixth field
                            )
                                   )
        return historical_list

