# dao/educational_content_dao.py

from typing import List, Tuple
from HU.Project.Website.entities.db_connection import Database


class EducationalContentDAO:
    @staticmethod
    def insert_content(topic: str, description: str):
        """Inserts new educational content into the database."""
        query = """
            INSERT INTO educational_content (topic, description)
            VALUES (%s, %s)
        """
        params = (topic, description)
        Database.execute_query(query, params)

    @staticmethod
    def fetch_content_by_id(content_id: int):
        """Fetches educational content by its ID."""
        query = "SELECT * FROM educational_content WHERE content_id = %s"
        params = (content_id,)
        return Database.fetch_one(query, params)

    @staticmethod
    def fetch_all_content():
        """Fetches all educational content."""
        query = "SELECT * FROM educational_content"
        return Database.fetch_all(query)

    @staticmethod
    def get_content_by_topic(topic: str):
        """
        Retrieves educational content from the database based on the given topic.
        """
        query = "SELECT * FROM educational_content WHERE contentType = %s"
        result = Database.execute_query(query, (topic,))

        if result:
            # Return a simple dictionary, no entity involved here
            return {
                'content_id': result[0]['content_id'],
                'topic': result[0]['topic'],
                'body': result[0]['body']
            }
        else:
            raise ValueError(f"No content found for topic: {topic}")
