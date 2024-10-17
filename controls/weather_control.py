from HU.Project.Website.entities.weather_data import WeatherData


# controls/view_weather_control.py
class WeatherControl:
    def get_latest_weather(self, location: str):
        """
        Executes the use case to fetch the latest weather data for a location.
        """
        weather_data = WeatherData.get_latest_weather(location)
        return weather_data
