# boundaries/health_advisory_boundary.py
from HU.Project.Website.controls.alert_control import AlertControl


class HealthAdvisoryBoundary:
    def check_advisories(self, user_id: int):
        """
        Passes the user ID to the control object to check health advisories.
        """
        control = AlertControl()
        return control.check_health_advisory(user_id)
