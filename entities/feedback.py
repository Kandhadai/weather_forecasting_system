# entities/feedback.py

from typing import Dict, List, Tuple
from HU.Project.Website.dao.feedback_dao import FeedbackDAO


class Feedback:
    def __init__(self, user_id: int,username: str, feedback_type: str, message: str):
        #self.feedback_id = feedback_id
        self.user_id = user_id
        self.username = username
        self.feedback_type = feedback_type
        self.message = message
        #self.submitted_at = submitted_at

    @staticmethod
    def submit_feedback(user_id: int, username: str, feedback_type: str, message: str):
        """Submits a new feedback."""
        FeedbackDAO.insert_feedback(user_id, username,feedback_type, message)

    @staticmethod
    def get_feedback_by_id(feedback_id: int):
        """Retrieves feedback by its ID."""
        result = FeedbackDAO.fetch_feedback_by_id(feedback_id)
        if result:
            return Feedback(
                #feedback_id=result['feedback_id'],
                user_id=result['user_id'],
                username= result['username'],
                feedback_type=result['feedback_type'],
                message=result['message'],
                #submitted_at=result['submitted_at']
            )
        return None

    @staticmethod
    def get_all_feedback():
        """Retrieves all feedback."""
        results = FeedbackDAO.fetch_all_feedback()
        feedbacks = []
        for result in results:
            feedbacks.append(Feedback(
                #feedback_id=result['feedback_id'],
                user_id=result['user_id'],
                username=result['username'],
                feedback_type=result['feedback_type'],
                message=result['message'],
                #submitted_at=result['submitted_at']
            ))
        return feedbacks
