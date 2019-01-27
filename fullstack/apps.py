from django.apps import AppConfig


class FullstackConfig(AppConfig):
    name = 'fullstack'

    def ready(self):
        from fullstack import signals  # noqa
