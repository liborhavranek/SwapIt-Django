"""
Author: Made with love by Libor Raven
Date: 16.10.2024
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from .utils import get_registration_test_user_data

User = get_user_model()


class LoginPageTest(TestCase):
    """Testy pro přihlašovací stránku"""

    def setUp(self) -> None:
        """Nastavení testovacího uživatele"""
        data = get_registration_test_user_data()
        self.client.post(reverse('registration'), data)

    def test_login_page_status_code(self) -> None:
        """Testuje zda má přihlašovací stránka vrací správný response"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_template(self) -> None:
        """Testuje zda má přihlašovací stránka správnou šablonu"""
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_login_valid_user_username_redirects_to_home(self) -> None:
        """Testuje úspěšné přihlášení uživatele s platnými údaji"""
        data = {
            'username_or_email': 'testuser',
            'password': 'complex_password_123'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertRedirects(response, reverse('home'))

    def test_login_valid_user_email_redirects_to_home(self) -> None:
        """Testuje úspěšné přihlášení uživatele s platnými údaji"""
        data = {
            'username_or_email': 'testuser@example.com',
            'password': 'complex_password_123'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertRedirects(response, reverse('home'))

    def test_login_valid_user_username_creates_session(self) -> None:
        """Testuje zda úspěšné přihlášení vytvoří session pro uživatele"""
        data = {
            'username_or_email': 'testuser',
            'password': 'complex_password_123'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_valid_user_email_creates_session(self) -> None:
        """Testuje zda úspěšné přihlášení vytvoří session pro uživatele"""
        data = {
            'username_or_email': 'testuser@example.com',
            'password': 'complex_password_123'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_user_shows_error_message(self) -> None:
        """Testuje přihlášení s neplatnými údaji"""
        data = {
            'username_or_email': 'testuser',
            'password': 'wrong_password'
        }
        response = self.client.post(reverse('login'), data)
        self.assertContains(response, "Nesprávné přihlašovací údaje. Zkuste to znovu.")
