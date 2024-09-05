from django.contrib import admin
from django.urls import path
from core.views import get_services_by_master, MainView, ThanksTemplateView
from django.conf.urls.static import static
from django.conf import settings
# as_view() - говорим чтобы пути смогли воспринимать класс

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),
    path("get_services_by_master/<int:master_id>/", get_services_by_master, name="get_services_by_master"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)