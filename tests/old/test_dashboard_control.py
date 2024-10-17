# tests/test_dashboard_control.py
import pytest
from HU.Project.Website.controls.dashboard_settings_control import CustomizeDashboardControl


def test_save_dashboard_settings(mocker):
    mocker.patch('HU.Project.Website.entities.DashboardSettings.DashboardSettings.save', return_value=None)

    control = CustomizeDashboardControl()
    assert control.save_settings(1, {'theme': 'dark'}) is None
