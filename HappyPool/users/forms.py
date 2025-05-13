from django import forms

from .models import UserProfile


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'profile_photo', 'license']
