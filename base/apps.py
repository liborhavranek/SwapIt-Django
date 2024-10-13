"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    Konfigurační třída pro aplikaci 'base'.
    Nastavuje výchozí typ automaticky generovaného primárního klíče
    na 'BigAutoField' a definuje název aplikace jako 'base'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
