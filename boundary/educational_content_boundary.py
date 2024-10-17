# boundaries/educational_content_boundary.py

from HU.Project.Website.controls.educational_content_control import EducationalContentControl
from flask import request


# boundaries/educational_content_boundary.py
class EducationalContentBoundary:
    def get_content(self, topic: str):
        """
        Passes the educational topic to the control object to fetch the content.
        """
        topic = request.form.get('topic')
        control = EducationalContentControl()
        return control.get_content_by_topic(topic)
