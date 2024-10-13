"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Registruje hlavní stránku"""
    template_name = 'home.html'
