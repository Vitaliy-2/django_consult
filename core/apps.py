from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Записи клиентов'

    # По готовности приложения будет импортирован сигнал
    def ready(self):
        import core.signals
