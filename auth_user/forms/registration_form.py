"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class UserRegisterForm(UserCreationForm):
    """
    Formulář pro registraci uživatele s přidanými poli pro jméno, příjmení, a e-mail.
    Obsahuje také vlastní validace pro uživatelské jméno a email, aby se zajistilo,
    že se nebudou duplikovat existující hodnoty v databázi.
    """
    first_name = forms.CharField(
        label='Jméno',
        required=True,
        max_length=30,
        validators=[MinLengthValidator(2)],
        error_messages={
            'required': 'Jméno je povinné pole.',
            'min_length': 'Jméno musí mít alespoň 2 znaky.',
            'max_length': 'Jméno může mít maximálně 30 znaků.',
        }
    )
    last_name = forms.CharField(
        label='Příjmení',
        required=True,
        max_length=30,
        validators=[MinLengthValidator(2)],
        error_messages={
            'required': 'Příjmení je povinné pole.',
            'min_length': 'Příjmení musí mít alespoň 2 znaky.',
            'max_length': 'Příjmení může mít maximálně 30 znaků.',
        }
    )
    username = forms.CharField(
        label='Přihlašovací jméno',
        required=True,
        max_length=30,
        validators=[MinLengthValidator(2)],
        error_messages={
            'required': 'Přihlašovací jméno je povinné pole.',
            'min_length': 'Přihlašovací jméno musí mít alespoň 2 znaky.',
            'max_length': 'Přihlašovací jméno může mít maximálně 30 znaků.',
        }
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        error_messages={
            'required': 'Email je povinné pole.',
            'invalid': 'Zadejte platnou emailovou adresu.',
        }
    )
    password1 = forms.CharField(
        label='Heslo',
        strip=False,
        widget=forms.PasswordInput,
        help_text=None,
        error_messages={
            'required': 'Zadejte heslo.',
            'min_length': 'Heslo musí mít alespoň 8 znaků.',
        }
    )
    password2 = forms.CharField(
        label='Potvrďte heslo',
        strip=False,
        widget=forms.PasswordInput,
        help_text=None,
        error_messages={
            'required': 'Potvrďte své heslo.',
            'min_length': 'Heslo musí mít alespoň 8 znaků.',
        }
    )

    class Meta:
        """Nastavuje model a pole, která budou použita v tomto formuláři."""
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self) -> str:
        """
       Zajišťuje, že emailová adresa není již použita jiným uživatelem.
       """
        email: str = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Tento email je již používán.')
        return email

    def clean_username(self) -> str:
        """Zajišťuje, že přihlašovací jméno není již použito jiným uživatelem."""
        username: str = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Přihlašovací jméno je již používáno.')
        return username

    def clean_password2(self) -> str:
        """Kontroluje, zda jsou obě zadaná hesla stejná."""
        password1: str = self.cleaned_data.get('password1')
        password2: str = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Hesla se neshodují.')
        return password2
