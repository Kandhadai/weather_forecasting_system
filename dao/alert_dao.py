# dao/alert_dao.py
from typing import List, Tuple
from HU.Project.Website.entities.db_connection import Database


class AlertDAO:
    @staticmethod
    def insert_alert(user_id: int, alert_type: str, conditions: str):
        """Inserts a new alert into the database."""
        query = """
            INSERT INTO alerts (user_id, alert_type, conditions)
            VALUES (%s, %s, %s)
        """
        params = (user_id, alert_type, conditions)
        Database.execute_query(query, params)

    @staticmethod
    def fetch_alert_by_id(alert_id: int):
        """Fetches an alert from the database by its ID."""
        query = "SELECT * FROM alerts WHERE alert_id = %s"
        params = (alert_id,)
        return Database.fetch_one(query, params)

    @staticmethod
    def fetch_alerts_for_user(user_id: int):
        """Fetches all alerts for a specific user."""
        query = "SELECT * FROM alerts WHERE user_id = %s"
        params = (user_id,)
        return Database.fetch_all(query, params)

    @staticmethod
    def delete_alert(alert_id: int):
        """Deletes an alert from the database by its ID."""
        query = "DELETE FROM alerts WHERE alert_id = %s"
        params = (alert_id,)
        Database.execute_query(query, params)
