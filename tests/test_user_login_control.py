# tests/test_user_login_control.py
import pytest
from HU.Project.Website.controls.user_login_control import UserLoginControl
from HU.Project.Website.entities.user import User


def test_authenticate_success(mocker):
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_username',
                 return_value=User(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))
    mocker.patch('HU.Project.Website.entities.user.User.authenticate', return_value=True)

    control = UserLoginControl()
    assert control.authenticate("sriraman", "Lonewolf@31") is True


def test_authenticate_failure(mocker):
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_username',
                 return_value=None)  # Simulate user not found

    control = UserLoginControl()
    assert control.authenticate("wrong_user", "wrong_password") is False


def test_reset_password(mocker):
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_username',
                 return_value=User(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))
    mocker.patch('HU.Project.Website.entities.user.User.hash_password', return_value="new_hashed_password")
    mocker.patch('HU.Project.Website.entities.user.User.save', return_value=None)

    control = UserLoginControl()
    assert control.reset_password("test_user", "new_password123") is True


def test_update_user_location(mocker):
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_id',
                 return_value=User(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))
    mocker.patch('HU.Project.Website.entities.user.User.save', return_value=None)

    control = UserLoginControl()
    control.update_user_location(1, "Los Angeles")

    user = User.get_user_by_id(1)
    assert user.location == "Los Angeles"


def test_get_user_id(mocker):
    # Mock the User entity method to return a user with a specific ID
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_username',
                 return_value=User(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))

    control = UserLoginControl()
    user_id = control.get_user_id("test_user")

    assert user_id == 1


def test_get_user_id_fail(mocker):
    # Mock the User entity method to return None when the user is not found
    mocker.patch('HU.Project.Website.entities.user.User.get_user_by_username', return_value=None)

    control = UserLoginControl()
    user_id = control.get_user_id("non_existent_user")

    assert user_id == -1

