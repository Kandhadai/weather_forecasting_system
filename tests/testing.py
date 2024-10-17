from HU.Project.Website.entities.alert import Alert
from HU.Project.Website.dao.user_dao import UserDAO
from HU.Project.Website.entities.user import User

# def test_alert_dao_create_alert():
#     # Assuming we have a setup to interact with a test database
#     #dao = AlertDAO()
#     alert_id = Alert.create_alert(1, "temperature", ">30")
#
#     # Assert that a valid ID was returned, meaning the alert was successfully created
#     assert alert_id is not None
#
#     saved_alerts = Alert.get_alerts_for_user(1)
#s
#     # Iterate over all alerts and check the properties
#     for alert in saved_alerts:
#         assert alert.alert_type == "temperature"
#         assert alert.condition == ">30"


# def authenticate(username: str, password: str) -> bool:
#     """
#     Authenticates the user by username and password.
#     """
#     try:
#         # Fetch the user instance using a method within the User entity
#         user = User.get_user_by_username(username)
#
#         # Use the entity's authenticate method to verify the password
#         if user and user.authenticate(password):
#             return True
#     except ValueError as e:
#         print(f"Authentication failed: {str(e)}")
#     return False
#
# # # Declare username and password as variables
# # username = None
# # password = None
#
# # Get user input for username and password
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# # Authenticate the user
# if authenticate(username, password):
#     print("Authentication successful!")
# else:
#     print("Authentication failed.")

from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, date

# Use TYPE_CHECKING to prevent runtime circular imports
if TYPE_CHECKING:
    from HU.Project.Website.dao.weather_dao import WeatherDataDAO

class WeatherData:
    def __init__(self, location, temperature, conditions, humidity, wind_speed, date):
        self.location = location
        self.temperature = temperature
        self.conditions = conditions
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.date = date

def get_latest_weather(location):
    """Fetches the latest weather data for the specified location from the database."""
    weather_data = WeatherDataDAO.fetch_latest_weather(location)
    if weather_data:
        return WeatherData(location=weather_data['location'], temperature=weather_data['temperature'],
                           conditions=weather_data['conditions'], humidity=weather_data['humidity'],
                           wind_speed=weather_data['wind_speed'], date=weather_data['date'])
    return None

# Get user input for username and password
location = input("Enter username: ")




