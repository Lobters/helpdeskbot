from django.db import models


class TelegramUserManager(models.Manager):
    def create_user_from_json(self, user_object):
        id = user_object.get('id')
        is_bot = user_object.get('is_bot')
        first_name = user_object.get('first_name')
        last_name = user_object.get('last_name')
        username = user_object.get('username')
        language_code = user_object.get('language_code')
        user = TelegramUser.objects.create(id=id, is_bot=is_bot, first_name=first_name, last_name=last_name,
                                           username=username, language_code=language_code)
        user.save()


class TelegramUser(models.Model):
    objects = TelegramUserManager()
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    language_code = models.CharField(default='ru', max_length=4)

    def __str__(self):
        return str(self.username)