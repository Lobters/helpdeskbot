import datetime

from django.db import models


class TelegramUserManager(models.Manager):
    def create_user_from_json(self, user_object):
        id = user_object.get('id')
        is_bot = user_object.get('is_bot')
        first_name = user_object.get('first_name')
        last_name = user_object.get('last_name')
        username = user_object.get('username')
        language_code = user_object.get('language_code')
        user = self.objects.create(id=id, is_bot=is_bot, first_name=first_name, last_name=last_name,
                                   username=username, language_code=language_code)
        user.save()


class TelegramUser(models.Model):
    objects = TelegramUserManager()
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField(blank=True, default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    language_code = models.CharField(default='ru', max_length=4)

    def __str__(self):
        return str(self.username)


class TelegramChatManager(models.Manager):
    def create_chat_from_json(self, chat_object):
        id = chat_object.get('id')
        first_name = chat_object.get('first_name', '')
        last_name = chat_object.get('last_name', '')
        username = chat_object.get('username', '')
        type = chat_object.get('type', '')
        chat = self.objects.create(id=id, first_name=first_name, last_name=last_name, username=username,
                                   type=type)
        chat.save()


class TelegramChat(models.Model):
    objects = TelegramChatManager
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    TYPES = (
        ("pr", 'private'),
        ('gr', 'group'),
        ('su', 'supergroup'),
        ('ch', 'channel'),
    )
    type = models.CharField(max_length=15, choices=TYPES)

    def __str__(self):
        return self.first_name or self.id


class TelegramMessageManager(models.Manager):
    def create_message_from_json(self, message_object, user, chat):
        message_id = message_object.get('message_id')
        text = message_object.get('text')
        message = self.objects.create(message_id=message_id, user=user, chat=chat, text=text)
        message.save()


class TelegramMessage(models.Model):
    objects = TelegramMessageManager
    message_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    chat = models.ForeignKey(TelegramChat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=270)

    def __str__(self):
        return self.user
