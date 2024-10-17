from HU.Project.Website.entities.db_connection import Database
from typing import List, Tuple


class HealthAdvisoryDAO:
    @staticmethod
    def fetch_all_advisories():
        """Fetches all health advisories from the database."""
        query = "SELECT * FROM health_advisories"
        result = Database.fetch_all(query)
        return result

