from HU.Project.Website.entities.alert import Alert


def test_create_alert(mocker):
    mocker.patch('HU.Project.Website.dao.alert_dao.AlertDAO.create_alert', return_value=101)

    alert = Alert.create_alert(1, "temperature", ">30")
    assert alert.alert_id == 101
    assert alert.alert_type == "temperature"
    assert alert.condition == ">30"


def test_get_alerts_for_user(mocker):
    mocker.patch('HU.Project.Website.dao.alert_dao.AlertDAO.get_alerts_for_user',
                 return_value=[(1, 1, "temperature", ">30"), (2, 1, "humidity", "<60")])

    alerts = Alert.get_alerts_for_user(1)
    assert len(alerts) == 2
    assert alerts[0].alert_type == "temperature"
    assert alerts[1].alert_type == "humidity"


def test_save_new_alert(mocker):
    mocker.patch('HU.Project.Website.dao.alert_dao.AlertDAO.create_alert', return_value=101)

    alert = Alert(1, "temperature", ">30")
    alert.save()
    assert alert.alert_id == 101  # New alert created


def test_save_existing_alert(mocker):
    mocker.patch('HU.Project.Website.dao.alert_dao.AlertDAO.update_alert', return_value=None)

    alert = Alert(1, "temperature", ">30", alert_id=1)
    alert.save()
    assert alert.alert_id == 1  # Existing alert updated
