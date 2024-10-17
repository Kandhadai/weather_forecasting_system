# entities/dashboard_settings.py

from typing import Dict
from HU.Project.Website.dao.DashboardSettings_dao import DashboardDAO


class Dashboard:
    """
        Represents user-specific dashboard settings.
        """

    def __init__(self, user_id: int, settings: Dict[str, any] = None):
        self.user_id = user_id
        self.settings = settings if settings is not None else self.apply_default_settings()

    def load(self):
        """
        Loads the dashboard settings for the user from the database using the DAO.
        """
        # Import inside the method to avoid circular dependency
        from HU.Project.Website.dao.DashboardSettings_dao import DashboardDAO
        loaded_settings = DashboardDAO.load_settings(self.user_id)
        if loaded_settings:
            self.settings = loaded_settings.settings

    def save(self):
        """
        Saves the current settings to the database using the DAO.
        """
        # Import inside the method to avoid circular dependency
        from HU.Project.Website.dao.DashboardSettings_dao import DashboardDAO
        DashboardDAO.save_settings(self)

    def update_setting(self, key: str, value: any):
        """
        Updates a specific setting for the user.
        """
        self.settings[key] = value
        self.save()

    def remove_setting(self, key: str):
        """
        Removes a specific setting for the user.
        """
        if key in self.settings:
            del self.settings[key]
            self.save()

    def get_setting(self, key: str):
        """
        Retrieves the value of a specific setting.
        """
        return self.settings.get(key)

    @staticmethod
    def apply_default_settings() -> Dict[str, any]:
        """
        Applies a set of default settings if no settings exist.
        """
        default_settings = {
            "theme": "light",
            "notifications": True,
            "layout": "grid"
        }
        return default_settings
