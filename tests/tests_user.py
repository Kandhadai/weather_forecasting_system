from HU.Project.Website.controls.user_login_control import UserLoginControl
from HU.Project.Website.entities.user import User
import logging
import sys
from datetime import datetime
import pytest, hashlib


def test_validate_user():
    valid_user = User(1, "test_user", "test_user@example.com", "Address", "Location", "hashed_pass")
    invalid_user_1 = User(1, "", "test_user@example.com", "Address", "Location", "hashed_pass")
    invalid_user_2 = User(1, "test_user", "invalid_email", "Address", "Location", "hashed_pass")

    assert valid_user.validate_user() is True
    assert invalid_user_1.validate_user() is False
    assert invalid_user_2.validate_user() is False


def test_authenticate():
    user = User(1, "test_user", "test_user@example.com", "Address", "Location",
                hashlib.sha256("password123".encode()).hexdigest())

    assert user.authenticate("password123") is True
    assert user.authenticate("wrong_password") is False

def test_authenticate_user():
    user = User(user_id=1, username='test_user', email='valid@example.com', address='123 Main St', location='NY', password_hash=User.hash_password('correct_password'))
    assert user.authenticate('correct_password') is True
    assert user.authenticate('wrong_password') is False

def test_update_location():
    user = User(1, "test_user", "test_user@example.com", "Address", "Old Location", "hashed_pass")

    # Valid location
    user.update_location("New York")
    assert user.location == "New York"

    # Invalid location
    with pytest.raises(ValueError):
        user.update_location("Invalid#Location")


def test_hash_password():
    password_1 = "password123"
    password_2 = "secretPass!"

    assert User.hash_password(password_1) == hashlib.sha256(password_1.encode()).hexdigest()
    assert User.hash_password(password_2) == hashlib.sha256(password_2.encode()).hexdigest()

def test_validate_location():
    assert User.validate_location('New York') is True
    assert User.validate_location('Invalid#Location') is False

def test_save_user(mocker):
    mocker.patch('HU.Project.Website.entities.user.UserDAO.update_user', return_value=None)
    user = User(user_id=1, username='test_user', email='valid@example.com', address='123 Main St', location='NY', password_hash='hash')
    user.save()
    assert True  # No errors mean success


def test_get_user_by_username(mocker):
    # Mock the UserDAO method to return a tuple representing a user
    mocker.patch('HU.Project.Website.dao.user_dao.UserDAO.get_user_by_username',
                 return_value=(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))

    user = User.get_user_by_username("test_user")

    assert user.user_id == 1
    assert user.username == "test_user"
    assert user.email == "test@test.com"

def test_get_user_by_id(mocker):
    # Mock the UserDAO method to return a tuple representing a user
    mocker.patch('HU.Project.Website.dao.user_dao.UserDAO.get_user_by_id',
                 return_value=(1, "test_user", "test@test.com", "123 Street", "New York", "hashed_password"))

    user = User.get_user_by_id(1)

    assert user.user_id == 1
    assert user.username == "test_user"
    assert user.email == "test@test.com"


