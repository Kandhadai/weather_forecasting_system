from HU.Project.Website.entities.weather_data import WeatherData
import datetime


def test_is_severe_weather():
    weather_data_1 = WeatherData("CityA", -15, 50, 120, "Clear", datetime.date.today())
    weather_data_2 = WeatherData("CityB", 25, 60, 80, "Clear", datetime.date.today())

    assert weather_data_1.is_severe_weather() is True  # Severe due to low temperature and high wind speed
    assert weather_data_2.is_severe_weather() is False  # Normal weather conditions


def test_suggest_weather_appropriate_clothing():
    cold_weather = WeatherData("CityA", -5, 60, 10, "Snow", datetime.date.today())
    hot_weather = WeatherData("CityB", 35, 50, 5, "Sunny", datetime.date.today())
    normal_weather = WeatherData("CityC", 22, 40, 8, "Cloudy", datetime.date.today())

    assert cold_weather.suggest_weather_appropriate_clothing() == "Wear warm clothing"
    assert hot_weather.suggest_weather_appropriate_clothing() == "Wear light clothing and stay hydrated"
    assert normal_weather.suggest_weather_appropriate_clothing() == "Dress comfortably"


def test_get_historical_data(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_historical_data', return_value=[
        WeatherData("CityA", 10, 50, 20, "Cloudy", datetime.date(2023, 1, 1)),
        WeatherData("CityA", 12, 48, 22, "Rain", datetime.date(2023, 1, 2))
    ])

    weather_data = WeatherData.get_historical_data("CityA", "2023-01-01", "2023-01-10")
    assert len(weather_data) == 2
    assert weather_data[0].temperature == 10
    assert weather_data[1].conditions == "Rain"


def test_weather_data_to_dict():
    weather_data = WeatherData("CityA", 15, 55, 10, "Cloudy", datetime.date.today())
    weather_dict = weather_data.to_dict()

    assert weather_dict["location"] == "CityA"
    assert weather_dict["temperature"] == 15
    assert weather_dict["conditions"] == "Cloudy"


def test_get_latest_weather(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_latest_weather',
                 return_value=WeatherData("New York", 25, 65, 8, "Clear", "2023-01-01"))

    weather = WeatherData.get_latest_weather("New York")
    assert weather.temperature == 25
    assert weather.conditions == "Clear"


def test_get_today_forecast(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_today_forecast',
                 return_value=WeatherData("New York", 30, 60, 5, "Sunny", "2023-01-01"))

    forecast = WeatherData.get_today_forecast("New York")
    assert forecast.temperature == 30
    assert forecast.conditions == "Sunny"


def test_get_extended_forecast(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_extended_forecast', return_value=[
        WeatherData("New York", 25, 60, 10, "Clear", "2023-01-02"),
        WeatherData("New York", 28, 58, 12, "Sunny", "2023-01-03")
    ])

    forecast = WeatherData.get_extended_forecast("New York", 3)
    assert len(forecast) == 2
    assert forecast[0].temperature == 25
    assert forecast[1].conditions == "Sunny"


def test_get_historical_data(mocker):
    mocker.patch('HU.Project.Website.dao.weather_dao.WeatherDataDAO.fetch_historical_data', return_value=[
        WeatherData("New York", 22, 50, 10, "Snow", "2023-01-01"),
        WeatherData("New York", 25, 55, 12, "Cloudy", "2023-01-02"),
    ])

    historical_data = WeatherData.get_historical_data("New York", "2023-01-01", "2023-01-05")
    assert len(historical_data) == 2
    assert historical_data[0].conditions == "Snow"
    assert historical_data[1].temperature == 25

