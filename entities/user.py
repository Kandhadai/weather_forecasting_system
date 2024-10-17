# entities/user.py

import hashlib
import re
from typing import Optional
from HU.Project.Website.dao.user_dao import UserDAO


class User:
    def __init__(self, user_id, username, email, address=None, location=None, password_hash=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.address = address
        self.location = location
        self.password_hash = password_hash

    def authenticate(self, password):
        """Compares the given password with the hashed password."""
        provided_password_hash = hashlib.sha256(password.encode()).hexdigest()
        return provided_password_hash == self.password_hash

    def reset_password(self, new_password):
        """Resets the user's password."""
        self.password_hash = self.hash_password(new_password)
        #print(self.user_id)
        UserDAO.update_user_password(self.user_id, self.password_hash)

    @classmethod
    def get_user_by_username(cls, username: str):
        """
        Retrieves a user object based on the self using UserDAO.
        """
        user_data = UserDAO.get_user_by_username(username)
        if user_data:
            return User(*user_data)
        raise ValueError(f"User with self '{username}' not found.")

    def get_user_by_id(self, user_id):
        """Retrieves a user by ID."""
        user_data = UserDAO.get_user_by_id(user_id)
        if user_data:
            return User(user_id=user_data['user_id'], username=user_data['username'], email=user_data['email'],
                        address=user_data.get('address'), location=user_data.get('location'),
                        password_hash=user_data['password_hash'])
        return None

    @staticmethod
    def hash_password(password):
        """Hashes a password using SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def signup(username: str, email: str, password: str, location: str, address: str = None) -> bool:
        """
        This method handles creating a new user and saving it to the database.
        """
        password_hash = User.hash_password(password)
        #print(password_hash)
        new_user = User(user_id=None, username=username, email=email, password_hash=password_hash, address=address,
                        location=location)

        # Save the new user using the DAO
        return UserDAO.create_user(new_user)
