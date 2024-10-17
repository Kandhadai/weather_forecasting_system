# entities/educational_content.py

from typing import List
from HU.Project.Website.dao.EducationalContent_dao import EducationalContentDAO


class EducationalContent:
    def __init__(self, content_id: int, topic: str, description: str):
        self.content_id = content_id
        self.topic = topic
        self.description = description

    @staticmethod
    def create_content(topic: str, description: str):
        """Creates a new educational content."""
        EducationalContentDAO.insert_content(topic, description)

    @staticmethod
    def get_content_by_id(content_id: int):
        """Fetches educational content by its ID."""
        result = EducationalContentDAO.fetch_content_by_id(content_id)
        if result:
            return EducationalContent(
                content_id=result['content_id'],
                topic=result['topic'],
                description=result['description']
            )
        return None

    @staticmethod
    def get_all_content():
        """Fetches all educational content."""
        results = EducationalContentDAO.fetch_all_content()
        contents = []
        for result in results:
            contents.append(EducationalContent(
                content_id=result['content_id'],
                topic=result['topic'],
                description=result['description']
            ))
        return contents

    @staticmethod
    def get_content_by_topic(topic: str):
        """
        Retrieves educational content for the given topic using DAO.
        This is an entity-level static method, which delegates the data fetching to DAO.
        """
        content_data = EducationalContentDAO.get_content_by_topic(topic)

        # Return an instance of EducationalContent with the fetched data
        return EducationalContent(
            content_id=content_data['content_id'],
            topic=content_data['topic'],
            description=content_data['description']
        )
