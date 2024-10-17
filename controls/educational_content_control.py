from HU.Project.Website.entities.educational_content import EducationalContent


# controls/educational_content_control.py
class EducationalContentControl:
    def get_content_by_topic(self, topic: str):
        """
        Executes the use case to retrieve educational content based on the topic.
        """
        content = EducationalContent.get_content_by_topic(topic)
        return content

