from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    This class creates a poll object
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
