# tests/test_weather_control.py
import pytest
from HU.Project.Website.controls.weather_control import ViewWeatherControl
from HU.Project.Website.entities.weather_data import WeatherData


def test_get_latest_weather(mocker):
    mock_weather = WeatherData(location='New York', temperature=25, humidity=60, wind_speed=10, conditions='Sunny',
                               date='2024-09-17')
    mocker.patch('HU.Project.Website.entities.weather_data.WeatherData.get_latest_weather', return_value=mock_weather)

    control = ViewWeatherControl()
    weather = control.get_latest_weather('New York')
    assert weather.temperature == 25
    assert weather.conditions == 'Sunny'
