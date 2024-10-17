# dao/user_dao.py

from HU.Project.Website.entities.db_connection import Database
from typing import Optional
import flash


class UserDAO:
    @staticmethod
    def create_user(user):
        """Inserts a new user into the database."""
        # Database logic to insert a new user
        query = """
        INSERT INTO users (username, email, password_hash, address, location) 
        VALUES (%s, %s, %s, %s, %s)
        """
        #print(user.username)
        values = (user.username, user.email, user.password_hash, user.address, user.location)
        try:
            rows_affected = Database.execute_query(query, values)
            #print(rows_affected)
            if rows_affected > 0:
                print(f"User {user.username} created successfully")
                return True
            else:
                print(f"Failed to create user {user.username}")
                return False
        except Exception as e:
            print(f"Error creating user {user.username}: {e}")
            return False

    # @staticmethod
    # def get_user_by_username(username: str):
    #     """
    #     Fetches raw user data (not an entity) from the database by username.
    #     """
    #     query = "SELECT user_id, username, password_hash FROM users WHERE username = %s"
    #     result = Database.fetch_one(query, (username,))
    #     if result:
    #         return result  # This returns raw data, not a User entity
    #     return None

    @staticmethod
    def get_user_by_username(username: str) -> tuple:
        """
        Retrieves a user from the database by their self.
        Returns a tuple of user details instead of a User object.
        """
        query = "SELECT user_id, username, email, address, location, password_hash FROM users WHERE username = %s"
        params = (username,)
        result = Database.fetch_one(query, params)
        return result

    @staticmethod
    def get_user_by_id(user_id):
        """Retrieves a user from the database by their user ID."""
        query = "SELECT * FROM users WHERE user_id = %s"
        result = Database.fetch_one(query, (user_id,))
        return result

    @staticmethod
    def update_user_password(user_id, new_password_hash):
        """Updates the password of an existing user."""
        query = "UPDATE users SET password_hash = %s WHERE user_id = %s"
        Database.execute_query(query, (new_password_hash, user_id))

    @staticmethod
    def get_user_location(user_id: int) -> str:
        """
        Retrieves the user's location based on their user ID.
        """
        query = "SELECT location FROM users WHERE user_id = %s"
        print(query)
        result = Database.execute_query(query, (user_id,))

        if result:
            return result[0]  # Return the location if found
        else:
            return None




