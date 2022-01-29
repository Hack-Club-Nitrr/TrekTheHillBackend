from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation',
                    )


admin.site.register(Team, TeamAdmin)
