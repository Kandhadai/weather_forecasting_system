# entities/alert.py
from typing import List, Optional
from HU.Project.Website.dao.alert_dao import AlertDAO


class Alert:
    def __init__(self, alert_id: int, user_id: int, alert_type: str, condition: str):
        self.alert_id = alert_id
        self.user_id = user_id
        self.alert_type = alert_type
        self.condition = condition
        #self.created_at = created_at

    @staticmethod
    def create_alert(user_id: int, alert_type: str, condition: str):
        """Creates a new alert for a user."""
        AlertDAO.insert_alert(user_id, alert_type, condition)

    @staticmethod
    def get_alert_by_id(alert_id: int):
        """Retrieves an alert by its ID."""
        result = AlertDAO.fetch_alert_by_id(alert_id)
        if result:
            return Alert(
                alert_id=result['alert_id'],
                user_id=result['user_id'],
                alert_type=result['alert_type'],
                condition=result['condition']
                #,created_at=result['created_at']
            )
        return None

    @staticmethod
    def get_alerts_for_user(user_id: int):
        """Retrieves all alerts for a specific user."""
        results = AlertDAO.fetch_alerts_for_user(user_id)
        alerts = []
        for result in results:
            alerts.append(Alert(
                alert_id=result['alert_id'],
                user_id=result['user_id'],
                alert_type=result['alert_type'],
                condition=result['condition']
                #,created_at=result['created_at']
            ))
        return alerts

    @staticmethod
    def delete_alert(alert_id: int):
        """Deletes an alert by its ID."""
        AlertDAO.delete_alert(alert_id)

    @classmethod
    def find_by_user_id(cls, user_id: int):
        """
        Find all alerts for a specific user by user_id.
        """
        alerts_data = AlertDAO.fetch_alerts_for_user(user_id)  # Assuming AlertDAO fetches the data
        alerts = []

        for data in alerts_data:
            alert = cls(
                alert_id=data[0],
                user_id=data[1],
                alert_type=data[2],
                condition=data[3]
            )
            alerts.append(alert)

        return alerts
