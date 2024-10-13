"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.apps import AppConfig


class AuthUserConfig(AppConfig):
    """
    Konfigurační třída pro aplikaci 'auth_user'.
    Nastavuje výchozí typ automaticky generovaného primárního klíče
    na 'BigAutoField' a definuje název aplikace jako 'auth_user'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_user'
