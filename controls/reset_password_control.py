from HU.Project.Website.entities.user import User


class ResetPasswordControl:
    def reset_password(self, username, new_password):
        user = User.get_user_by_username(username)
        if user:
            #print(f"User found: {user.username}")
            user.reset_password(new_password)
            return True
        return False
