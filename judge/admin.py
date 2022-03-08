from django.contrib import admin
from .models import Judge


class JudgeAdmin(admin.ModelAdmin):
    list_display = ('name','email')


admin.site.register(Judge, JudgeAdmin)
