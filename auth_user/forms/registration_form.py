# auth_user/registration_form.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class UserRegisterForm(UserCreationForm):
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
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Tento email je již používán.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Přihlašovací jméno je již používáno.')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Hesla se neshodují.')
        return password2
