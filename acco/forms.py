from django.contrib.auth.forms import UserCreationForm
from  .models import AccountsUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AccountsUser
        fields = ('username', 'email', 'password1', 'password2')