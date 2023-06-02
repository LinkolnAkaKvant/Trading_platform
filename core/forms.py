from django.contrib.auth.forms import UserCreationForm
from core.models import User


class UserCreatedForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    