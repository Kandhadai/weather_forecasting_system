# boundaries/user_login_boundary.py

from HU.Project.Website.controls.user_login_control import UserLoginControl


# boundaries/user_login_boundary.py
class UserLoginBoundary:
    @staticmethod
    def login(request):
        """
        Collects login data from the form submission.
        """
        username = request.form.get('username')
        password = request.form.get('password')
        return username, password




