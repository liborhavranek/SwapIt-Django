"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.test import TestCase
from auth_user.forms.registration_form import UserRegisterForm


class TestUserRegisterFormLabels(TestCase):
    """Testuje, registrační formulář zda má všechny pole labely"""
    def test_first_name_field_label(self) -> None:
        """Testuje, zda pole 'first_name' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['first_name'].label, 'Jméno')

    def test_last_name_field_label(self) -> None:
        """Testuje, zda pole 'last_name' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['last_name'].label, 'Příjmení')

    def test_username_field_label(self) -> None:
        """Testuje, zda pole 'username' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['username'].label, 'Přihlašovací jméno')

    def test_email_field_label(self) -> None:
        """Testuje, zda pole 'email' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['email'].label, 'Email')

    def test_password1_field_label(self) -> None:
        """Testuje, zda pole 'password1' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['password1'].label, 'Heslo')

    def test_password2_field_label(self) -> None:
        """Testuje, zda pole 'password2' má správný label."""
        form = UserRegisterForm()
        self.assertEqual(form.fields['password2'].label, 'Potvrďte heslo')


class TestUserRegisterForm(TestCase):
    """Testuje, registrační formulář zda má správnou validaci."""
    def test_first_name_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'first_name'."""
        form = UserRegisterForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())

    def test_first_name_in_errors(self) -> None:
        """Testuje, že pole 'first_name' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'first_name': ''})
        form.is_valid()
        self.assertIn('first_name', form.errors)

    def test_first_name_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'first_name'."""
        form = UserRegisterForm(data={'first_name': ''})
        form.is_valid()
        self.assertEqual(form.errors['first_name'], ['Jméno je povinné pole.'])

    def test_last_name_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'last_name'."""
        form = UserRegisterForm(data={'last_name': ''})
        self.assertFalse(form.is_valid())

    def test_last_name_in_errors(self) -> None:
        """Testuje, že pole 'last_name' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'last_name': ''})
        form.is_valid()
        self.assertIn('last_name', form.errors)

    def test_last_name_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'last_name'."""
        form = UserRegisterForm(data={'last_name': ''})
        form.is_valid()
        self.assertEqual(form.errors['last_name'], ['Příjmení je povinné pole.'])

    def test_username_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'username'."""
        form = UserRegisterForm(data={'username': ''})
        self.assertFalse(form.is_valid())

    def test_username_in_errors(self) -> None:
        """Testuje, že pole 'username' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'username': ''})
        form.is_valid()
        self.assertIn('username', form.errors)

    def test_username_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'username'."""
        form = UserRegisterForm(data={'username': ''})
        form.is_valid()
        self.assertEqual(form.errors['username'], ['Přihlašovací jméno je povinné pole.'])


class TestUserRegisterFormEmailAndPass(TestCase):
    """Testuje, registrační formulář zda má správnou validaci email a heslo."""
    def test_email_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'email'."""
        form = UserRegisterForm(data={'email': ''})
        self.assertFalse(form.is_valid())

    def test_email_in_errors(self) -> None:
        """Testuje, že pole 'email' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'email': ''})
        form.is_valid()
        self.assertIn('email', form.errors)

    def test_email_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'email'."""
        form = UserRegisterForm(data={'email': ''})
        form.is_valid()
        self.assertEqual(form.errors['email'], ['Email je povinné pole.'])

    def test_password1_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'password1'."""
        form = UserRegisterForm(data={'password1': ''})
        self.assertFalse(form.is_valid())

    def test_password1_in_errors(self) -> None:
        """Testuje, že pole 'password1' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'password1': ''})
        form.is_valid()
        self.assertIn('password1', form.errors)

    def test_password1_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'password1'."""
        form = UserRegisterForm(data={'password1': ''})
        form.is_valid()
        self.assertEqual(form.errors['password1'], ['Zadejte heslo.'])

    def test_password2_required_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný bez vyplněného pole 'password2'."""
        form = UserRegisterForm(data={'password2': ''})
        self.assertFalse(form.is_valid())

    def test_password2_in_errors(self) -> None:
        """Testuje, že pole 'password2' je obsaženo v chybách, pokud není vyplněno."""
        form = UserRegisterForm(data={'password2': ''})
        form.is_valid()
        self.assertIn('password2', form.errors)

    def test_password2_required_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'password2'."""
        form = UserRegisterForm(data={'password2': ''})
        form.is_valid()
        self.assertEqual(form.errors['password2'], ['Potvrďte své heslo.'])

    def test_email_invalid_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný s neplatnou emailovou adresou."""
        form = UserRegisterForm(data={'email': 'invalidemail'})
        self.assertFalse(form.is_valid())

    def test_email_invalid_in_errors(self) -> None:
        """Testuje, že pole 'email' je obsaženo v chybách s neplatnou adresou."""
        form = UserRegisterForm(data={'email': 'invalidemail'})
        form.is_valid()
        self.assertIn('email', form.errors)

    def test_email_invalid_error_message(self) -> None:
        """Testuje, že se zobrazuje správná chybová zpráva pro pole 'email'."""
        form = UserRegisterForm(data={'email': 'invalidemail'})
        form.is_valid()
        self.assertEqual(form.errors['email'], ['Zadejte platnou emailovou adresu.'])

    def test_password1_min_length_is_invalid(self) -> None:
        """Testuje, že formulář je neplatný s příliš krátkým heslem."""
        form = UserRegisterForm(data={'password1': 'short'})
        self.assertFalse(form.is_valid())
