from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from .views import login_view, logout_view, register_view


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', next_page='main'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='/'
    ), name='register'),
]


# path('logout/', LogoutView.as_view(next_page='main', http_method_names=['get', 'post'], template_name="logout.html"), name='logout'),
# Пока что выход (logout) осуществляется через функцию во views
