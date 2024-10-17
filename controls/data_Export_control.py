# controls/data_export_control.py

from HU.Project.Website.entities.data_export import DataExport


# controls/export_data_control.py
class DataExportControl:
    def export_data(self, user_id: int, format: str, location: str, start_date: str, end_date: str):
        """
        Executes the events in the use case: export data for the given location and date range.
        """
        # Proceed with exporting the data
        data_export = DataExport(user_id)
        export_path = data_export.export_weather_data(format, location, start_date, end_date)
        data_export.log_export(export_path, format)  # Now the entity handles logging
        return export_path



