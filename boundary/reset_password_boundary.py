# boundaries/reset_password_boundary.py
from HU.Project.Website.controls.user_login_control import UserLoginControl


class ResetPasswordBoundary:
    def reset_password(self, request):
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        return username, new_password
