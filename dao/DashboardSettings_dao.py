# dao/dashboard_settings_dao.py
from HU.Project.Website.entities.db_connection import Database
import json


class DashboardDAO:
    """
        Handles database operations for DashboardSettings.
        """

    @staticmethod
    def _connect_to_db():
        return Database.connect()

    @classmethod
    def save_settings(cls, dashboard_settings):
        """
        Saves or updates the dashboard settings for a user.
        """
        connection = cls._connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            "REPLACE INTO dashboard_settings (user_id, settings) VALUES (%s, %s)",
            (dashboard_settings.user_id, str(dashboard_settings.settings))
        )
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def load_settings(cls, user_id: int):
        """
        Loads the dashboard settings for a specific user.
        Returns settings as a dictionary or None if no settings are found.
        """
        connection = cls._connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT settings FROM dashboard_settings WHERE user_id = %s",
            (user_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            try:
                # Use JSON to safely parse the settings stored as a string
                settings = json.loads(result[0])
                return settings
            except json.JSONDecodeError:
                return None
        else:
            return None
