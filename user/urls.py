from django.urls import path
from .views import (
    logout_view,
    CustomLoginView,
    CustomRegisterView,
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path("password_change/", CustomPasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", CustomPasswordChangeDoneView.as_view(), name="password_change_done"),
    
]


# path('logout/', LogoutView.as_view(next_page='main', http_method_names=['get', 'post'], template_name="logout.html"), name='logout'),
# Пока что выход (logout) осуществляется через функцию во views
