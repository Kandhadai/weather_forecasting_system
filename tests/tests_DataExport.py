from HU.Project.Website.entities.data_export import DataExport
from HU.Project.Website.entities.weather_data import WeatherData
import json, datetime


def test_export_weather_data_csv(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_historical_data', return_value=[
        WeatherData("New York", 22, 50, 10, "Sunny", "2023-01-01"),
        WeatherData("New York", 23, 55, 12, "Cloudy", "2023-01-02"),
    ])

    export = DataExport(1)
    file_path = export.export_weather_data("csv", "New York", "2023-01-01", "2023-01-10")

    assert file_path == "weather_data_1.csv"
    # Read the file to ensure it's correctly written
    with open(file_path, 'r') as f:
        lines = f.readlines()
        assert lines[1] == "2023-01-01,22,50,10,Sunny\n"
        assert lines[2] == "2023-01-02,23,55,12,Cloudy\n"


def test_log_export(mocker):
    mocker.patch('HU.Project.Website.dao.dataexport_dao.DataExportDAO.log_export', return_value=None)

    export = DataExport(1)
    result = export.log_export("weather_data_1.csv", "csv")

    assert result is None  # The log_export method should not return any values


def test_get_export_history(mocker):
    mocker.patch('HU.Project.Website.dao.dataexport_dao.DataExportDAO.get_export_history', return_value=[
        ("weather_data_1.csv", "csv"),
        ("weather_data_2.json", "json")
    ])

    export = DataExport(1)
    history = export.get_export_history()

    assert len(history) == 2
    assert history[0] == ("weather_data_1.csv", "csv")


def test_export_weather_data_json(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_historical_data', return_value=[
        WeatherData("New York", 22, 50, 10, "Sunny", "2023-01-01"),
        WeatherData("New York", 23, 55, 12, "Cloudy", "2023-01-02"),
    ])

    export = DataExport(1)
    file_path = export.export_weather_data("json", "New York", "2023-01-01", "2023-01-10")

    assert file_path == "weather_data_1.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
        assert data[0]["temperature"] == 22
        assert data[1]["conditions"] == "Cloudy"
