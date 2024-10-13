# auth_user/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from auth_user.forms.registration_form import UserRegisterForm
from django.contrib import messages


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{form.fields[field].label}: {error}')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Registrace byla úspěšná.')
        return super().form_valid(form)
