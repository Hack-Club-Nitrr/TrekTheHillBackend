from django.contrib import admin
from .models import Sponser


class SponserAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Sponser, SponserAdmin)
