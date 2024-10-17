# controls/view_historical_data_control.py
from HU.Project.Website.entities.weather_data import WeatherData


class HistoricalDataControl:
    def get_historical_data(self, location: str, start_date: str, end_date: str):
        """
        Executes the use case to fetch historical weather data for a location and date range.
        """
        historical_data = WeatherData.get_historical_data(location, start_date, end_date)
        return historical_data
