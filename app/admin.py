from django.contrib import admin

from .models import *

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'default_status')

admin.site.register(Application, ApplicationAdmin)
