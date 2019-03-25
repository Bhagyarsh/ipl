from django.contrib import admin
from django import forms
from .models import (results,question, match)
from iplcrew.models import IPLTeam,iplplayer

from .forms import questionAdminForm,resultAdminForm
# Register your models here.

class questionAdmin(admin.ModelAdmin):
    form = questionAdminForm
class resultAdmin(admin.ModelAdmin):
    form = resultAdminForm
admin.site.register(match)
admin.site.register(question,questionAdmin)
admin.site.register(results,resultAdmin)
