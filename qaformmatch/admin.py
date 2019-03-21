from django.contrib import admin
from .models import (question_toss,question_winner,question_mostrun,question_mostsixes,
                        question_mostwickets,question_mostboundaries,question_mom)
# Register your models here.
admin.site.register(question_toss)
admin.site.register(question_winner)
admin.site.register(question_mostrun)
admin.site.register(question_mostsixes)
admin.site.register(question_mostwickets)
admin.site.register(question_mostboundaries)
admin.site.register(question_mom)
