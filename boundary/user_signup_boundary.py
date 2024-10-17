# boundaries/user_signup_boundary.py
from HU.Project.Website.controls.user_signup_control import UserSignupControl
from flask import request

class UserSignupBoundary:
    def signup(self, request):
        """
        This method takes signup data and passes it to the control object.
        """
        username = request.form.get('username')
        #print(username)
        email = request.form.get('email')
        #print(email)# Fallback to form data if email is not provided
        password = request.form.get('password')  # Fallback to form data if password is not provided
        confirm_password = request.form.get('confirm_password')
        address = request.form.get('address')
        location = request.form.get('location')

        return username, email, password, confirm_password, address, location
