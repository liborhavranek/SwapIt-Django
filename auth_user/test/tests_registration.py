"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .utils import get_registration_test_user_data


class RegistrationPageTest(TestCase):
    """Testy pro registrační stránku"""
    def test_registration_page_status_code(self) -> None:
        """Testuje zda má registrační stránka vrací správný response"""
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_page_template(self) -> None:
        """Testuje zda má registrační stránka správnou šablonu"""
        response = self.client.get(reverse('registration'))
        self.assertTemplateUsed(response, 'registration.html')

    def test_register_valid_user_have_response_302(self) -> None:
        """Testuje úspěšnou registraci uživatele s platnými údaji včetně jména a příjmení"""
        data = get_registration_test_user_data()
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 302)

    def test_register_valid_user_save_user_in_db(self) -> None:
        """Testuje úspěšnou registraci uživatele s platnými údaji včetně jména a příjmení"""
        data = get_registration_test_user_data()
        self.client.post(reverse('registration'), data)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    class RegistrationPageTestInvalid(TestCase):
        """Testy pro registrační stránku s nevalidními argumenty"""
    def test_register_user_no_first_name_page_show_message(self) -> None:
        """Testuje registraci uživatele bez Jména"""
        data = {
            'first_name': '',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Jméno je povinné pole.")

    def test_register_user_short_first_name_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš krátkým jménem"""
        data = {
            'first_name': 'T',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Jméno musí mít alespoň 2 znaky.")

    def test_register_user_long_first_name_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš dlouhým příjmením"""
        data = {
            'first_name': 'T'*31,
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Jméno může mít maximálně 30 znaků.")

    def test_register_user_no_last_name_page_show_message(self) -> None:
        """Testuje registraci uživatele bez příjmení"""
        data = {
            'first_name': 'Test',
            'last_name': '',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Příjmení je povinné pole.")

    def test_register_user_short_last_name_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš krátkým příjmením"""
        data = {
            'first_name': 'Test',
            'last_name': 'U',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Příjmení musí mít alespoň 2 znaky.")

    def test_register_user_long_last_name_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš dlouhým příjmením"""
        data = {
            'first_name': 'Test',
            'last_name': 'U' * 31,
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Příjmení může mít maximálně 30 znaků.")

    def test_register_user_no_username_page_show_message(self) -> None:
        """Testuje registraci uživatele bez přihlašovacího jména"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Přihlašovací jméno je povinné pole.")

    def test_register_user_short_username_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš krátkým přihlašovacím jménem"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'T',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Přihlašovací jméno musí mít alespoň 2 znaky.")

    def test_register_user_long_username_page_show_message(self) -> None:
        """Testuje registraci uživatele s příliš dlouhým přihlašovacím jménem"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'T' * 31,
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Přihlašovací jméno může mít maximálně 30 znaků.")

    def test_register_user_duplicate_username_page_show_message(self) -> None:
        """Testuje registraci uživatele s již existujícím přihlašovacím jménem"""
        User.objects.create_user(username='testuser', email='existing@example.com', password='password123')
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Přihlašovací jméno je již používáno.")

    def test_register_user_duplicate_username_not_saved_in_db(self) -> None:
        """Testuje, že duplicitní přihlašovací jméno nebylo uloženo do databáze"""
        User.objects.create_user(username='testuser', email='existing@example.com', password='password123')

        data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        self.client.post(reverse('registration'), data)
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)


class RegistrationPageTestInvalidEmailAndPass(TestCase):
    """Testy pro registrační stránku s nevalidními argumenty email a heslo"""
    def test_register_user_no_email_page_show_message(self) -> None:
        """Testuje registraci uživatele bez vyplněného emailu"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': '',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Email je povinné pole.")

    def test_register_user_invalid_email_page_show_message(self) -> None:
        """Testuje registraci uživatele s neplatným formátem emailu"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'invalid-email',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Zadejte platnou emailovou adresu.")

    def test_register_user_duplicate_email_page_show_message(self) -> None:
        """Testuje registraci uživatele s již existujícím emailem"""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'existing@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, "Tento email je již používán.")

    def test_register_user_duplicate_email_not_saved_in_db(self) -> None:
        """Testuje, že duplicitní email není uložen do databáze"""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'existing@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        self.client.post(reverse('registration'), data)
        self.assertEqual(User.objects.filter(email='existing@example.com').count(), 1)

    def test_password_too_short_user_is_not_saved_in_db(self) -> None:
        """Testuje registraci s příliš krátkým heslem."""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'short',
            'password2': 'short',
        }
        self.client.post(reverse('registration'), data)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_passwords_do_not_match(self) -> None:
        """Testuje registraci, když se hesla neshodují."""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'different_password_123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, 'Hesla se neshodují.')

    def test_passwords_do_not_match_user_is_not_saved_in_db(self) -> None:
        """Testuje registraci, když se hesla neshodují."""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'different_password_123',
        }
        self.client.post(reverse('registration'), data)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_password_minimum_length(self) -> None:
        """Testuje registraci s heslem, které splňuje minimální délku."""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
        }
        self.client.post(reverse('registration'), data)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_password_missing(self) -> None:
        """Testuje registraci bez zadaného hesla."""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': '',
            'password2': '',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertContains(response, 'Zadejte heslo.')
