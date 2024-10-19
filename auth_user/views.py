"""
Author: Made with love by Libor Raven
Date: 13.10.2024
"""
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib import messages

from auth_user.forms.login_form import CustomAuthenticationForm
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


class LoginView(FormView):
    """Třída pro testování přihlášení"""
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: CustomAuthenticationForm) -> HttpResponse:
        user = form.cleaned_data.get('user')
        login(self.request, user)
        messages.success(self.request, 'Přihlášení proběhlo úspěšně.')
        return super().form_valid(form)

    def form_invalid(self, form: CustomAuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Nesprávné přihlašovací údaje. Zkuste to znovu.')
        return super().form_invalid(form)


class LogoutView(View):
    """Třída pro odhlášení uživatele"""
    def get(self, request: HttpRequest) -> HttpResponseRedirect:
        """Odhlášení uživatele"""
        logout(request)
        messages.success(request, 'Odhlášení proběhlo úspěšně.')
        return HttpResponseRedirect(reverse_lazy('home'))
