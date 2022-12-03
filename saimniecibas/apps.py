from django.apps import AppConfig


class SaimniecibasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'saimniecibas'

    def ready(self):
        import saimniecibas.signals
