# controls/submit_feedback_control.py
from HU.Project.Website.entities.feedback import Feedback


class FeedbackControl:
    def submit_feedback(self, user_id, username,feedback_type, message):
        """
        Business logic to submit feedback.
        """
        feedback = Feedback.submit_feedback(user_id=user_id, username=username, feedback_type=feedback_type, message=message)
        return feedback




