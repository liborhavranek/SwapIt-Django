"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    """Testovací třída pro kontrolu funkčnosti domovské stránky."""
    def test_home_page_status_code(self) -> None:
        """Testuje, zda domovská stránka vrací správný HTTP status kód 200 (OK)."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self) -> None:
        """Testuje, zda je pro domovskou stránku použit správný šablonový soubor 'home.html'."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
