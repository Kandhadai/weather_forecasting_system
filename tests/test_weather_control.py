# tests/test_weather_control.py
import pytest
from HU.Project.Website.controls.weather_control import ViewWeatherControl
from HU.Project.Website.entities.weather_data import WeatherData


def test_get_latest_weather(mocker):
    # Mock the DAO method to return weather data
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_latest_weather',
                 return_value=WeatherData("New York", 25, 60, 10, "Clear", "2024-09-29"))

    weather = WeatherData.get_latest_weather("New York")

    assert weather.location == "New York"
    assert weather.temperature == 25
    assert weather.conditions == "Clear"


def test_get_historical_data(mocker):
    # Mock the DAO method to return historical data
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_historical_data',
                 return_value=[WeatherData("New York", 25, 60, 10, "Clear", "2024-09-01"),
                               WeatherData("New York", 30, 55, 12, "Sunny", "2024-09-02")])

    historical_data = WeatherData.get_historical_data("New York", "2024-09-01", "2024-09-10")

    assert len(historical_data) == 2
    assert historical_data[0].temperature == 25
    assert historical_data[1].conditions == "Sunny"


def test_get_extended_forecast(mocker):
    # Mock the DAO method to return forecast data
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_extended_forecast',
                 return_value=[WeatherData("New York", 25, 60, 10, "Clear", "2024-09-29"),
                               WeatherData("New York", 28, 65, 8, "Cloudy", "2024-09-30")])

    extended_forecast = WeatherData.get_extended_forecast("New York", 7)

    assert len(extended_forecast) == 2
    assert extended_forecast[0].conditions == "Clear"
    assert extended_forecast[1].conditions == "Cloudy"


def test_get_today_forecast(mocker):
    # Mock the WeatherData.get_today_forecast method
    mocker.patch('HU.Project.Website.entities.weather_data.WeatherData.get_today_forecast', return_value=WeatherData('New York',
                                    25, 50, 10, 'Clear', '2023-09-28'))

    control = ViewWeatherControl()
    forecast = control.get_today_forecast('New York')

    assert forecast.location == 'New York'
    assert forecast.temperature == 25
    assert forecast.conditions == 'Clear'



