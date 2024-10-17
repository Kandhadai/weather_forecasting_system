# tests/test_feedback_control.py
import pytest
from HU.Project.Website.controls.feedback_control import FeedbackControl


def test_submit_feedback(mocker):
    # Mock the 'provide_feedback' method of the Feedback entity to avoid database operations
    mocker.patch('HU.Project.Website.entities.feedback.Feedback.provide_feedback', return_value=1)

    control = FeedbackControl()
    result = control.submit_feedback(1, 'test_user', 'bug', 'This is a bug report')

    # Assert the returned message is the expected string
    assert result == 'Feedback submitted successfully.'
