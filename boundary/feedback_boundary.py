# boundaries/feedback_boundary.py

from HU.Project.Website.controls.feedback_control import FeedbackControl
from flask import request


class FeedbackBoundary:
    def submit_feedback(self, request):
        """
        Extracts the feedback details from the request object.
        """
        feedback_type = request.form.get('feedback_type')
        message = request.form.get('message')

        # Ensure that both feedback_type and message are provided
        if not feedback_type or not message:
            raise ValueError("Feedback type and message are required")

        return feedback_type, message


