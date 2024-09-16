from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomLoginForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('main')


def logout_view(request):
    # logout - выйти из системы
    logout(request)
    return redirect('main')


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
