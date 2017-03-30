from django.contrib import admin

from .models import GameUser

@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
	pass