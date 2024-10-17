# boundaries/today_forecast_boundary.py
from HU.Project.Website.controls.view_today_forecast_control import TodayForecastControl
from flask import Request


class TodayForecastBoundary:
    def get_today_forecast(self, request: Request):
        """
        Passes the location to the control object to get today's forecast.
        """
        location = request.args.get('location', 'New York')  # Default to 'New York'
        control = TodayForecastControl()
        return control.get_today_forecast(location)
