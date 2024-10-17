# tests/test_data_export_control.py
import pytest
from HU.Project.Website.controls.data_Export_control import ExportDataControl


def test_export_data(mocker):
    mocker.patch('HU.Project.Website.entities.data_export.DataExport.export_weather_data', return_value='data_export_1.csv')

    control = ExportDataControl()
    file_path = control.export_data(1, 'csv', 'New York', '2024-09-01', '2024-09-10')
    assert file_path == 'data_export_1.csv'


