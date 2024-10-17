# tests/test_alert_control.py
import pytest
from unittest.mock import patch
from HU.Project.Website.controls.alert_control import AlertControl
from HU.Project.Website.entities.alert import Alert
from HU.Project.Website.entities.weather_data import WeatherData
from HU.Project.Website.entities.user import User
from HU.Project.Website.entities.healthadvisory import HealthAdvisory


def test_create_user_alert(mocker):
    # Mock the Alert's save method to avoid database operations
    mocker.patch('HU.Project.Website.entities.alert.Alert.save', return_value=None)

    control = AlertControl()
    alert = control.create_user_alert(1, 'temperature', '>30')

    assert isinstance(alert, Alert)
    assert alert.user_id == 1
    assert alert.alert_type == 'temperature'
    assert alert.condition == '>30'


def test_check_health_advisory(mocker):
    # Mock user location retrieval
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_id',
                 return_value=User(user_id=1, username="test_user", email="test@test.com", address="123 Street",
                                   location="New York"))

    # Mock latest weather data
    mocker.patch('HU.Project.Website.entities.weather_data.WeatherData.get_latest_weather',
                 return_value=WeatherData(location="New York", temperature=35, humidity=60, wind_speed=10,
                                          conditions="hot", date="2024-09-29"))

    # Mock health advisories
    mocker.patch('HU.Project.Website.entities.healthadvisory.HealthAdvisory.get_all_advisories',
                 return_value=[HealthAdvisory(1, "hot", "Stay hydrated"),
                               HealthAdvisory(2, "cold", "Wear warm clothing")])

    control = AlertControl()
    advisories = control.check_health_advisory(1)

    assert len(advisories) == 1
    assert advisories[0].message == "Stay hydrated"


def test_get_user_alerts(mocker):
    # Mock the retrieval of user alerts
    mocker.patch('HU.Project.Website.entities.alert.Alert.get_alerts_for_user',
                 return_value=[Alert(user_id=1, alert_type='temperature', condition='>30', alert_id=1)])

    control = AlertControl()
    alerts = control.get_user_alerts(1)

    assert len(alerts) == 1
    assert alerts[0].alert_type == 'temperature'
    assert alerts[0].condition == '>30'

