from HU.Project.Website.controls.dashboard_settings_control import CustomizeDashboardControl
from HU.Project.Website.entities.DashboardSettings import DashboardSettings


def test_load_dashboard_settings(mocker):
    # Mock object for the return value of load_settings, having the "settings" attribute
    mock_dashboard_settings = DashboardSettings(1)  # Assuming DashboardSettings takes user_id as an argument
    mock_dashboard_settings.settings = {"theme": "dark"}  # Assign the expected settings

    # Mock the DAO's load_settings method to return the mock_dashboard_settings object
    mocker.patch('HU.Project.Website.dao.DashboardSettings_dao.DashboardSettingsDAO.load_settings',
                 return_value=mock_dashboard_settings)

    # Use the static method to load the dashboard settings
    settings = CustomizeDashboardControl.load_dashboard_settings(1)

    # Assert that the theme loaded is "dark"
    assert settings.settings["theme"] == "dark"


def test_save_dashboard_settings(mocker):
    # Mock the save_settings method to simulate saving without actual database interaction
    mocker.patch('HU.Project.Website.dao.DashboardSettings_dao.DashboardSettingsDAO.save_settings', return_value=None)

    # Use the static method to save the settings
    new_settings = {"theme": "dark"}
    CustomizeDashboardControl.save_settings(1, new_settings)

    # Assert that no exception was raised, meaning the save was successful
    assert True  # No exceptions mean success


