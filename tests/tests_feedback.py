from HU.Project.Website.entities.feedback import Feedback


def test_provide_feedback(mocker):
    mocker.patch('HU.Project.Website.dao.feedback_dao.FeedbackDAO.provide_feedback', return_value=101)

    feedback = Feedback.provide_feedback(1, "test_user", "bug", "Bug report")
    assert feedback.feedback_id == 101
    assert feedback.feedback_type == "bug"
    assert feedback.message == "Bug report"


def test_get_all_feedbacks(mocker):
    mocker.patch('HU.Project.Website.dao.feedback_dao.FeedbackDAO.get_all_feedbacks', return_value=[
        (1, 1, "test_user", "bug", "Bug report"),
        (2, 2, "another_user", "feature", "Feature request")
    ])

    feedbacks = Feedback.get_all_feedbacks()
    assert len(feedbacks) == 2
    assert feedbacks[0].feedback_type == "bug"
    assert feedbacks[1].feedback_type == "feature"
