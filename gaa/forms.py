from django import forms
from django.contrib.auth.models import User
from .models import GAAClub

class SignupForm(forms.ModelForm):
    favorite_club = forms.ModelChoiceField(
        queryset=GAAClub.objects.all()
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }