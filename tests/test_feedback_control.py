# tests/test_feedback_control.py
import pytest
from HU.Project.Website.controls.feedback_control import FeedbackControl


def test_submit_feedback(mocker):
    mocker.patch('HU.Project.Website.entities.feedback.Feedback.provide_feedback', return_value=1)

    control = FeedbackControl()
    result = control.submit_feedback(1, "test_user", "bug", "Found a bug")

    assert result == "Feedback submitted successfully."


