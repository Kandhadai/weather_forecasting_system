from HU.Project.Website.entities.alert import Alert
from HU.Project.Website.entities.healthadvisory import HealthAdvisory
from HU.Project.Website.entities.weather_data import WeatherData


# controls/alert_control.py
class AlertControl:
    def create_alert(self, user_id: int, alert_type: str, condition: str):
        """
        Executes the use case to create an alert for the user.
        """
        user_alert = Alert.create_alert(user_id, alert_type, condition)
        return user_alert

    def check_health_advisory(self, user_id: int):
        """
        Executes the use case to check for relevant health advisories.
        """
        advisories = HealthAdvisory.check_advisories(user_id)
        return advisories

    def get_user_alerts(self, user_id: int):
        """
        Fetches all alerts for a given user.
        """
        alerts = Alert.find_by_user_id(user_id)
        if alerts:
            return alerts
        else:
            raise ValueError(f"No alerts found for user ID {user_id}")

