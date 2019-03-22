from django.contrib import admin
from django import forms
from .models import (results,question, match)
from iplcrew.models import IPLTeam,iplplayer
from .forms import questionAdminForm
# Register your models here.

class questionAdmin(admin.ModelAdmin):
    form = questionAdminForm

admin.site.register(question,questionAdmin)
admin.site.register(results)
admin.site.register(match)