from django.contrib import admin
from .models import *


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_link', 'requirements', 'xp_level')
