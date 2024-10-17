# controls/user_login_control.py

from HU.Project.Website.entities.user import User


class UserLoginControl:

    @staticmethod
    def authenticate(username: str, password: str) -> bool:
        """
        Authenticates the user by username and password.
        """
        try:
            # Fetch the user instance using a method within the User entity
            user = User.get_user_by_username(username)

            # Use the entity's authenticate method to verify the password
            if user and user.authenticate(password):
                return True
        except ValueError as e:
            print(f"Authentication failed: {str(e)}")
        return False

    @staticmethod
    def get_user_id(username: str) -> int:
        """
        Control object for fetching user ID. It delegates the fetching of user ID to the User entity.
        """
        try:
            user = User.get_user_by_username(username)
            if user:
                return user.user_id
            return None
        except Exception as e:
            print(f"Error fetching user ID: {e}")
            return None

    def reset_password(self, username, new_password):
        """
        Resets the password for the given username.
        Returns:
            bool: True if password reset is successful, False otherwise.
        """
        # Retrieve the user entity by username
        user = User.get_user_by_username(username)

        if not user:
            return False

        # Set the new password
        user.password = new_password  # You should hash the password here for security reasons.

        # Save the updated user entity back to the database
        try:
            user.save()
            return True
        except Exception as e:
            print(f"Error resetting password: {e}")
            return False
