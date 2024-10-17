from HU.Project.Website.entities.db_connection import Database
from typing import List, Tuple


class FeedbackDAO:
    @staticmethod
    def insert_feedback(user_id: int, username: str,feedback_type: str, message: str):
        """Inserts a new feedback into the database."""
        query = """
            INSERT INTO feedback (user_id,username, feedback_type, message)
            VALUES (%s, %s,%s, %s)
        """
        params = (user_id,username, feedback_type, message)
        Database.execute_query(query, params)

    @staticmethod
    def fetch_feedback_by_id(feedback_id: int):
        """Fetches feedback by its ID."""
        query = "SELECT * FROM feedback WHERE feedback_id = %s"
        params = (feedback_id,)
        return Database.fetch_one(query, params)

    @staticmethod
    def fetch_all_feedback():
        """Fetches all feedback."""
        query = "SELECT * FROM feedback"
        return Database.fetch_all(query)
