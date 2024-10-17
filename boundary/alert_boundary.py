# boundaries/alert_boundary.py
from HU.Project.Website.controls.alert_control import AlertControl


class AlertBoundary:
    def create_alert(self, request):
        """
        Extracts alert type and condition from the request and returns them.
        """
        alert_type = request.form.get('alert_type')
        condition = request.form.get('condition')
        return alert_type, condition


