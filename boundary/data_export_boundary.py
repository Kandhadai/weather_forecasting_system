# boundaries/data_export_boundary.py

from HU.Project.Website.controls.data_Export_control import DataExportControl
from flask import request


# boundaries/data_export_boundary.py
class DataExportBoundary:
    def export_data(self, request):
        """
        Passes the data received from the actor to the control object.
        """
        export_format = request.form['format']
        location = request.form['location']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        return export_format, location, start_date, end_date

