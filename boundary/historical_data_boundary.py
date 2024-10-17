# boundaries/historical_data_boundary.py
from HU.Project.Website.controls.view_historical_data_control import HistoricalDataControl
from flask import Request


class HistoricalDataBoundary:
    def get_historical_data(self, request:Request):
        """
        Passes the location and date range to the control object to fetch historical data.
        """
        location = request.args.get('location', 'New York')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        control = HistoricalDataControl()
        return control.get_historical_data(location, start_date, end_date)
