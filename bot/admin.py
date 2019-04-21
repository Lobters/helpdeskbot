from django.contrib import admin

# Register your models here.
from bot.models import TelegramUser, TelegramChat

admin.site.register(TelegramUser)
admin.site.register(TelegramChat)
# admin.site.register(Message)
