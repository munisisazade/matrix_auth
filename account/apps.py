from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Hesab'

    def ready(self):
        import account.signals
