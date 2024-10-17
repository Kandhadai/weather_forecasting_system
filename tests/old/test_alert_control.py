# tests/test_alert_control.py
import pytest
from unittest.mock import patch
from HU.Project.Website.controls.alert_control import AlertControl
from HU.Project.Website.entities.alert import Alert


def test_create_user_alert(mocker):
    # Mock the save method of the Alert class to avoid database operations
    mocker.patch.object(Alert, 'save', return_value=None)

    control = AlertControl()
    alert = control.create_user_alert(1, 'temperature', '>30')

    # Ensure that the alert is created correctly and is of type Alert
    assert isinstance(alert, Alert)  # Check that the returned object is an instance of Alert
    assert alert.user_id == 1
    assert alert.alert_type == 'temperature'
    assert alert.condition == '>30'


# def test_create_user_alert(mocker):
#     mocker.patch('HU.Project.Website.entities.alert.Alert.create_alert', return_value=1)
#
#     control = AlertControl()
#     assert control.create_user_alert(1, 'temperature', '>30') is True
