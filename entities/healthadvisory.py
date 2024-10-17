from typing import List, TYPE_CHECKING
from HU.Project.Website.dao.health_advisory_dao import HealthAdvisoryDAO
from HU.Project.Website.dao.user_dao import UserDAO
from HU.Project.Website.entities.weather_data import WeatherData


class HealthAdvisory:
    def __init__(self, advisory_id, title, description, relevant_conditions):
        self.advisory_id = advisory_id
        self.title = title
        self.description = description
        self.relevant_conditions = relevant_conditions

    @staticmethod
    def get_all_advisories():
        """Retrieves all health advisories."""
        advisories_data = HealthAdvisoryDAO.fetch_all_advisories()
        advisories_list = []
        for data in advisories_data:
            advisories_list.append(HealthAdvisory(advisory_id=data['advisory_id'], title=data['title'],
                                                  description=data['description'], relevant_conditions=data['relevant_conditions']))
        return advisories_list

    def is_relevant_to_user(self, weather_data):
        """Checks if the health advisory is relevant to the user's current weather conditions."""
        if weather_data.conditions in self.relevant_conditions:
            return True
        return False

    @staticmethod
    def check_advisories(user_id: int):
        """
        Fetches the health advisories based on the user's current weather and conditions.
        """
        # Fetch the user's location
        user_location = UserDAO.get_user_location(user_id)

        # Fetch the latest weather data for the user's location
        current_weather = WeatherData.get_latest_weather(user_location)

        # Fetch all advisories and filter the relevant ones based on the current weather
        all_advisories = HealthAdvisoryDAO.fetch_all_advisories()
        relevant_advisories = [
            advisory for advisory in all_advisories if advisory.is_relevant_to_user(current_weather)
        ]

        return relevant_advisories
