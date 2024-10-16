"""
Author: Made with love by Libor Raven
Date: 14.10.2024
"""
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.http import HttpResponse


class CustomAuthenticationForm(forms.Form):
    """Třída pro přihlašovací formulář"""
    username_or_email = forms.CharField(
        label='Uživatelské jméno nebo e-mail')
    password = forms.CharField(widget=forms.PasswordInput,
                               label='Heslo')

    def clean(self) -> HttpResponse:
        """Funkce, která vyhledá uživatele podle jména nebo emailu"""
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')
        user = None
        if User.objects.filter(username=username_or_email).exists():
            user = authenticate(username=username_or_email, password=password)
        elif User.objects.filter(email=username_or_email).exists():
            user = authenticate(username=User.objects.get(email=username_or_email).username, password=password)

        if user is None:
            raise ValidationError('Nesprávné přihlašovací údaje')
        self.cleaned_data['user'] = user
        return self.cleaned_data
