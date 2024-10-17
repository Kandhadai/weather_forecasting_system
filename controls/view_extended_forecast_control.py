# controls/view_extended_forecast_control.py
from HU.Project.Website.entities.weather_data import WeatherData


class ExtendedForecastControl:
    def get_extended_forecast(self, location: str, days: int):
        """
        Executes the use case to get an extended forecast for a location.
        """
        extended_forecast = WeatherData.get_extended_forecast(location, days)
        return extended_forecast
