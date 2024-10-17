from HU.Project.Website.entities.db_connection import Database
from typing import List
import datetime

# Avoid direct import of WeatherData to prevent circular reference issues
from typing import TYPE_CHECKING


class WeatherDataDAO:

    def fetch_latest_weather(location):
        """Fetches the latest weather data for the given location from the database."""
        query = "SELECT * FROM weather_data WHERE location = %s ORDER BY date DESC LIMIT 1"
        result = Database.fetch_one(query, (location,))
        return result

    @staticmethod
    def fetch_today_forecast(location):
        """Fetches today's weather forecast for the given location."""
        query = "SELECT * FROM weather_data WHERE location = %s AND date = DATE('now')"
        result = Database.fetch_one(query, (location,))
        return result

    @staticmethod
    def fetch_extended_forecast(location, days):
        """Fetches an extended weather forecast for the given location and number of days."""
        query = """
           SELECT * FROM weather_data 
           WHERE location = %s 
           ORDER BY date ASC 
           LIMIT %s
           """
        try:
            # Execute the query and pass both location and days to fetch the extended forecast
            result = Database.fetch_all(query, (location, days))
            return result
        except Exception as e:
            print(f"Error fetching extended forecast: {e}")
            return None

    @staticmethod
    def fetch_historical_data(location, start_date, end_date):
        """Fetches historical weather data for the given location and date range."""
        query = "SELECT * FROM weather_data WHERE location = %s AND date BETWEEN %s AND %s"
        result = Database.fetch_all(query, (location, start_date, end_date))
        return result
