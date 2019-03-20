from django.contrib import admin
from .models import player,ipletable,IPLTeam,match
# Register your models here.
admin.site.register(player)
admin.site.register(ipletable)
admin.site.register(IPLTeam)
admin.site.register(match)