"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from auth_user.forms.registration_form import UserRegisterForm


class RegisterView(CreateView):
    """Třída pro inicializaci registrační stránky s registračním formulářem"""
    model = User
    form_class = UserRegisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form: UserRegisterForm) -> HttpResponse:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{form.fields[field].label}: {error}')
        return super().form_invalid(form)

    def form_valid(self, form: UserRegisterForm) -> HttpResponse:
        messages.success(self.request, 'Registrace byla úspěšná.')
        return super().form_valid(form)
