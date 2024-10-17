# boundaries/extended_forecast_boundary.py
from HU.Project.Website.controls.view_extended_forecast_control import ExtendedForecastControl
from flask import Request

class ExtendedForecastBoundary:
    @staticmethod
    def get_extended_forecast(request: Request):
        """
        Passes the location and number of days to the control object to get an extended forecast.
        """
        location = request.args.get('location', 'New York')  # Default to 'New York'
        days = request.args.get('days', 7, type=int)  # Default to 7 days if not provided

        # Pass the extracted values to the control object
        control = ExtendedForecastControl()
        return control.get_extended_forecast(location, days)
