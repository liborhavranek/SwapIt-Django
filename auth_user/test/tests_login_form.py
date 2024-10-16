"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.test import TestCase
from auth_user.forms.login_form import CustomAuthenticationForm


class TestUserRegisterFormLabels(TestCase):
    """Testuje, registrační formulář zda má všechny pole labely"""
    def test_username_or_email_field_label(self) -> None:
        """Testuje, zda pole 'first_name' má správný label."""
        form = CustomAuthenticationForm()
        self.assertEqual(form.fields['username_or_email'].label, 'Uživatelské jméno nebo e-mail')

    def test_password_field_label(self) -> None:
        """Testuje, zda pole 'last_name' má správný label."""
        form = CustomAuthenticationForm()
        self.assertEqual(form.fields['password'].label, 'Heslo')

    def test_username_or_email_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'first_name'."""
        form = CustomAuthenticationForm(data={'username_or_email': ''})
        self.assertFalse(form.is_valid())

    def test_password_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'first_name'."""
        form = CustomAuthenticationForm(data={'password': ''})
        self.assertFalse(form.is_valid())
