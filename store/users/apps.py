from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'store.users'

    def ready(self):
        import store.users.signals
