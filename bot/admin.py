from django.contrib import admin

# Register your models here.
from bot.models import TelegramUser

admin.site.register(TelegramUser)
# admin.site.register(Chat)
# admin.site.register(Message)
