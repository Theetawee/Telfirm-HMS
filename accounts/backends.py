from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Check if the username is provided
        if username is None:
            return None
        try:
            # Check if the user can be retrieved by username or email
            user = UserModel.objects.get(Q(username=username) | Q(email=username))

            # Verify the user's password
            if user.check_password(password):
                return user

        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
