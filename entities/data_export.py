# entities/data_export.py

from typing import List
from HU.Project.Website.entities.weather_data import WeatherData
from HU.Project.Website.dao.weather_dao import WeatherDataDAO
from HU.Project.Website.dao.dataexport_dao import DataExportDAO
import csv
import json
from datetime import date


class DataExport:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def export_weather_data(self, format: str, location: str, start_date: str, end_date: str) -> str:
        """
        Exports weather data for the user in the specified format, location, and time range.
        """
        # Retrieve weather data for the specified location and date range
        weather_data = WeatherDataDAO.fetch_historical_data(location, start_date, end_date)

        # Process and export data based on the specified format
        if format.lower() == 'csv':
            return self._export_to_csv(weather_data)
        elif format.lower() == 'json':
            return self._export_to_json(weather_data)
        else:
            raise ValueError("Unsupported format")

    def _export_to_csv(self, weather_data: List[WeatherData]) -> str:
        """
        Exports weather data to a CSV file.
        """
        csv_path = f"weather_data_{self.user_id}.csv"
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Temperature', 'Humidity', 'Wind Speed', 'Conditions'])  # Header row

            for data in weather_data:
                writer.writerow([data[0], data[1], data[2], data[3], data[4]])
        return csv_path

    def _export_to_json(self, weather_data):
        weather_data_dicts = []

        for data in weather_data:
            data_dict = {
                "Date": data[0],
                "Temperature": data[1],
                "Humidity": data[2],
                "Wind Speed": data[3],
                "Conditions": data[4]
            }
            weather_data_dicts.append(data_dict)

        with open('weather_data.json', 'w') as file:
            json.dump(weather_data_dicts, file, indent=4)

        return 'weather_data.json'

    def log_export(self, export_path: str, export_format: str):
        """
        Logs the export action into the database via DAO.
        """
        DataExportDAO.log_export(self, export_path, export_format)

    def get_export_history(self):
        """
        Retrieves the export history for the user using the DAO.
        """
        return DataExportDAO.get_export_history(self.user_id)
