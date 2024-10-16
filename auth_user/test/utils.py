"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from typing import Dict


def get_registration_test_user_data() -> Dict[str, str]:
    """Data pro registraci uživatele"""
    return {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'complex_password_123',
        'password2': 'complex_password_123',
    }
