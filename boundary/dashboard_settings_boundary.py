# boundaries/dashboard_settings_boundary.py

from HU.Project.Website.controls.dashboard_settings_control import DashboardSettingsControl


# boundaries/dashboard_settings_boundary.py
class DashboardSettingsBoundary:
    def save_dashboard_settings(self, request):
        # Extract the settings from the request form as a dictionary
        settings = request.form.to_dict()
        return settings

