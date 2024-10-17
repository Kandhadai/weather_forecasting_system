# controls/user_signup_control.py
from HU.Project.Website.entities.user import User


class UserSignupControl:
    def signup(self, username: str, email: str, password: str, location: str, address: str = None):
        """
        Executes the use case to handle user signup.
        """
        #print(username)
        #print(location)
        user = User.signup(username, email, password, address, location)
        if user:  # If the user creation is successful
            return True
        return False
