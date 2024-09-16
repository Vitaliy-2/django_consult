from django.urls import path
from .views import logout_view, CustomLoginView, CustomRegisterView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]


# path('logout/', LogoutView.as_view(next_page='main', http_method_names=['get', 'post'], template_name="logout.html"), name='logout'),
# Пока что выход (logout) осуществляется через функцию во views
