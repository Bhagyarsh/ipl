from django import forms
from django.db.models import Q
from django.contrib import admin
from iplcrew.models import  IPLTeam, iplplayer
from .models import question,match


class questionAdminForm(forms.ModelForm):
    class Meta:
        model = question
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super(questionAdminForm, self).__init__(*args, **kwargs)
        print(self.instance)
        if self.instance:
            team1 = self.instance.team1
            team2 = self.instance.team2
            self.fields['winner'].queryset = IPLTeam.objects.filter(
                Q(Teamname=team1) | Q(Teamname=team2))
            self.fields['tosswinner'].queryset = IPLTeam.objects.filter(
                Q(Teamname=team1) | Q(Teamname=team2))
            pk1 = IPLTeam.objects.get(Teamname=team1)
            pk2 = IPLTeam.objects.get(Teamname=team2)
            self.fields['player_mom'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostboundaries'].queryset =  iplplayer.objects.filter(Q(Teamname=pk1)|Q(Teamname=pk2))
            self.fields['player_mostrun'].queryset =  iplplayer.objects.filter(Q(Teamname=pk1)|Q(Teamname=pk2))
            self.fields['player_mostboundaries'].queryset =  iplplayer.objects.filter(Q(Teamname=pk1)|Q(Teamname=pk2))
            self.fields['player_mostsixs'].queryset =  iplplayer.objects.filter(Q(Teamname=pk1)|Q(Teamname=pk2))

class SupplierAdmin(admin.ModelAdmin):
    form = questionAdminForm
