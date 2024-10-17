# controls/health_advisory_control.py
from HU.Project.Website.entities.healthadvisory import HealthAdvisory


class HealthAdvisoryControl:
    def check_advisory(self, user_id: int):
        """
        Executes the use case to check health advisories for a user based on their current weather.
        """
        advisories = HealthAdvisory.check_advisories(user_id)
        return advisories
