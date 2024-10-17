# tests/test_user_login_control.py
import pytest
from HU.Project.Website.controls.user_login_control import UserLoginControl
from HU.Project.Website.entities.user import User


def test_authenticate_success(mocker):
    # Mocking the get_user_by_username method to return a User instance with all required parameters filled
    mocker.patch(
        'HU.Project.Website.controls.user_login_control.User.get_user_by_username',
        return_value=User(
            user_id=1,
            username='test',
            email='test@example.com',
            address='123 Test St',
            location='Testville',
            password_hash='hashed_pass'
        )
    )

    # Mocking the authenticate method to return True
    mocker.patch('HU.Project.Website.controls.user_login_control.User.authenticate', return_value=True)

    control = UserLoginControl()
    assert control.authenticate('test', 'password') is True


def test_authenticate_failure(mocker):
    # Mocking the get_user_by_username method to return None, simulating a user not found scenario
    mocker.patch('HU.Project.Website.controls.user_login_control.User.get_user_by_username', return_value=None)

    control = UserLoginControl()
    assert control.authenticate('wrong_user', 'password') is False
