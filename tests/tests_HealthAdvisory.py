from HU.Project.Website.entities.healthadvisory import HealthAdvisory


def test_create_advisory(mocker):
    mocker.patch('HU.Project.Website.dao.health_advisory_dao.HealthAdvisoryDAO.create_advisory',
                 return_value=(1, "High Temperature", "Avoid outdoor activities during peak heat hours."))

    advisory = HealthAdvisory.create_advisory("High Temperature", "Avoid outdoor activities during peak heat hours.")

    assert advisory.advisory_id == 1
    assert advisory.condition == "High Temperature"
    assert advisory.message == "Avoid outdoor activities during peak heat hours."


def test_get_all_advisories(mocker):
    mocker.patch('HU.Project.Website.dao.health_advisory_dao.HealthAdvisoryDAO.get_all_advisories', return_value=[
        (1, "High Temperature", "Avoid outdoor activities."),
        (2, "Low Humidity", "Stay hydrated.")
    ])

    advisories = HealthAdvisory.get_all_advisories()
    assert len(advisories) == 2
    assert advisories[0].condition == "High Temperature"
    assert advisories[1].message == "Stay hydrated."


def test_is_relevant_to_user(mocker):
    weather_data = mocker.Mock()
    weather_data.conditions = "High Temperature"

    advisory = HealthAdvisory(1, "High Temperature", "Avoid outdoor activities.")

    assert advisory.is_relevant_to_user(weather_data) is True

    advisory_different = HealthAdvisory(2, "Low Humidity", "Stay hydrated.")
    assert advisory_different.is_relevant_to_user(weather_data) is False


def test_update_advisory(mocker):
    mocker.patch('HU.Project.Website.dao.health_advisory_dao.HealthAdvisoryDAO.update_advisory',
                 return_value=(1, "Moderate Temperature", "No special precautions."))

    advisory = HealthAdvisory.update_advisory(1, "Moderate Temperature", "No special precautions.")

    assert advisory.advisory_id == 1
    assert advisory.condition == "Moderate Temperature"
    assert advisory.message == "No special precautions."


def test_delete_advisory(mocker):
    mocker.patch('HU.Project.Website.dao.health_advisory_dao.HealthAdvisoryDAO.delete_advisory', return_value=None)

    result = HealthAdvisory.delete_advisory(1)
    assert result is None  # The method should not return anything
