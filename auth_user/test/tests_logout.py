"""
Author: Made with love by Libor Raven
Date: 19.10.2024
"""
from django.test import TestCase
from django.urls import reverse
from auth_user.test.utils import get_registration_test_user_data


class LogoutTestCase(TestCase):
    """Testy pro odhlášení uživatele"""

    def setUp(self) -> None:
        """Nastavení testovacího uživatele"""
        data_login = {
            'username_or_email': 'testuser',
            'password': 'complex_password_123'
        }
        data = get_registration_test_user_data()
        self.client.post(reverse('registration'), data)
        self.client.post(reverse('login'), data_login, follow=True)

    def test_user_logout(self) -> None:
        """Testuje, zda se uživatel může odhlásit"""
        response = self.client.get(reverse('logout'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_is_redirected_to_home(self) -> None:
        """Testuje, zda je uživatel přesměrován"""
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

    def test_logout_without_login(self) -> None:
        """Testuje, zda se nepřihlášený uživatel pokusí o odhlášení"""
        response = self.client.get(reverse('logout'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
