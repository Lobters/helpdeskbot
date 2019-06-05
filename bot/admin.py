from django.contrib import admin

from .models import TelegramUser, TelegramChat, TelegramMessage

admin.site.register(TelegramUser)
admin.site.register(TelegramChat)
admin.site.register(TelegramMessage)
