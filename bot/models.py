from django.db import models


class TelegramUser(models.Model):
    id = models.IntegerField()
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    language_code = models.CharField(default='ru')
