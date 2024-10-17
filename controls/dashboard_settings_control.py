# control/dashboard_control.py

from HU.Project.Website.entities.DashboardSettings import Dashboard


# controls/customize_dashboard_control.py
class DashboardSettingsControl:

    @staticmethod
    def load_dashboard_settings(user_id: int) -> Dashboard:
        """
        Loads and returns the dashboard settings for a user.
        """
        settings = Dashboard(user_id)
        settings.load()
        return settings

    @staticmethod
    def customize_dashboard(user_id: int, new_settings: dict):
        """
        Customizes and saves new settings for the user's dashboard.
        """
        settings = Dashboard(user_id)
        settings.load()  # Load existing settings
        for key, value in new_settings.items():
            settings.update_setting(key, value)  # Update and save each setting

    @staticmethod
    def save_settings(user_id: int, settings: dict):
        """
        Saves or updates the user's dashboard settings.
        """
        dashboard_settings = Dashboard(user_id, settings)
        dashboard_settings.save()
