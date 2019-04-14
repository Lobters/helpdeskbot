from django.contrib import admin

# Register your models here.
from bot.models import TelegramUser

admin.site.register(TelegramUser)
