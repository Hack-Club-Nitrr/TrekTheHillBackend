from django.contrib import admin
from .models import Speaker


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


admin.site.register(Speaker, SpeakerAdmin)
