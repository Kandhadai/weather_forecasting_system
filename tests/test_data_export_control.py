# tests/test_data_export_control.py
import pytest
from HU.Project.Website.controls.data_Export_control import ExportDataControl
import os
import pymysql
import csv
from HU.Project.Website.entities.weather_data import WeatherData
from HU.Project.Website.entities.data_export import DataExport
from HU.Project.Website.entities.db_connection import DatabaseConnection


def test_export_data(mocker):
    mocker.patch('HU.Project.Website.entities.data_export.DataExport.export_weather_data',
                 return_value='weather_data.csv')
    mocker.patch('HU.Project.Website.entities.data_export.DataExport.log_export', return_value=None)

    control = ExportDataControl()
    export_path = control.export_data(1, "csv", "New York", "2024-01-01", "2024-01-07")

    assert export_path == 'weather_data.csv'


def test_export_weather_data_csv(mocker):
    # Mock the export_weather_data method to simulate data export
    mocker.patch.object(DataExport, 'export_weather_data', return_value="weather_data_1.csv")
    mocker.patch.object(DataExport, 'log_export', return_value=None)  # Mock the log export method

    control = ExportDataControl()
    export_path = control.export_data(1, "csv", "New York", "2023-09-01", "2023-09-07")

    # Verify that the export path is correct
    assert export_path == "weather_data_1.csv"


def setup_module():
    connection = DatabaseConnection.get_connection() # Use your database connection details
    cursor = connection.cursor()

    # Insert user with user_id 2 if it doesn't already exist
    cursor.execute(
        "INSERT INTO users (user_id, username,email,address,location,password_hash) VALUES (2, 'test_user','xyz@gmail.com',NULL,NULL,'hash_pass') ON DUPLICATE KEY UPDATE user_id=user_id;")
    connection.commit()
    cursor.close()
    connection.close()


def test_export_weather_data_json(mocker):
    # Mock the export_weather_data method to simulate data export
    mocker.patch.object(DataExport, 'export_weather_data', return_value="weather_data_2.json")
    mocker.patch.object(DataExport, 'log_export', return_value=None)  # Mock the log export method

    setup_module()
    control = ExportDataControl()
    export_path = control.export_data(2, "json", "Los Angeles", "2023-09-01", "2023-09-07")

    # Verify that the export path is correct
    assert export_path == "weather_data_2.json"


def test_export_weather_data_unsupported_format():
    control = ExportDataControl()

    # Expect a ValueError to be raised due to unsupported format
    with pytest.raises(ValueError) as exc_info:
        control.export_data(1, "xml", "New York", "2023-09-01", "2023-09-07")

    # Verify that the correct error message is raised
    assert str(exc_info.value) == "Unsupported format"


def test_get_export_history(mocker):
    # Mock the get_export_history method to return export history
    mock_history = [
        ("weather_data_1.csv", "csv"),
        ("weather_data_1.json", "json")
    ]
    mocker.patch.object(DataExport, 'get_export_history', return_value=mock_history)

    control = ExportDataControl()

    # Call the get_export_history method and verify the export history
    history = control.get_export_history(1)
    assert len(history) == 2
    assert history[0] == ("weather_data_1.csv", "csv")
    assert history[1] == ("weather_data_1.json", "json")

