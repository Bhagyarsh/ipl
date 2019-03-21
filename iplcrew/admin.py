from django.contrib import admin
from .models import iplplayer,ipletable,IPLTeam,match,result
# Register your models here.
admin.site.register(iplplayer)
admin.site.register(ipletable)
admin.site.register(IPLTeam)
admin.site.register(match)
admin.site.register(result)