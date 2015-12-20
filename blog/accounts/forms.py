from django import forms
from django.contrib.auth.models import User


# form to modify user's profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
