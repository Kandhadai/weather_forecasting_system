# controls/view_today_forecast_control.py
from HU.Project.Website.entities.weather_data import WeatherData



class TodayForecastControl:
    def get_today_forecast(self, location: str):
        """
        Executes the use case to get today's weather forecast for a location.
        """
        today_forecast = WeatherData.get_today_forecast(location)
        return today_forecast
