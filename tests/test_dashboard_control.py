# tests/test_dashboard_control.py
import pytest
from HU.Project.Website.controls.dashboard_settings_control import CustomizeDashboardControl
from HU.Project.Website.entities.DashboardSettings import DashboardSettings


def test_load_dashboard_settings(mocker):
    # Mock the load method of DashboardSettings to simulate loading settings
    mocker.patch('HU.Project.Website.entities.DashboardSettings.DashboardSettings.load', return_value=None)

    # Call the control method
    control = CustomizeDashboardControl()
    settings = control.load_dashboard_settings(1)

    # Assert that the settings object is an instance of DashboardSettings
    assert isinstance(settings, DashboardSettings)


def test_customize_dashboard(mocker):
    mocker.patch('HU.Project.Website.entities.DashboardSettings.DashboardSettings.save', return_value=None)

    control = CustomizeDashboardControl()
    control.customize_dashboard(1, {"theme": "dark", "layout": "list"})

    assert True  # No exceptions mean success


def test_save_settings(mocker):
    mocker.patch('HU.Project.Website.entities.DashboardSettings.DashboardSettings.save', return_value=None)

    control = CustomizeDashboardControl()
    control.save_settings(1, {"theme": "dark", "notifications": True})

    assert True  # No exceptions mean success
