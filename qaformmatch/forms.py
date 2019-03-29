from django import forms
from django.db.models import Q
from django.contrib import admin
from iplcrew.models import IPLTeam, iplplayer
from .models import question, match,results
from django.contrib.auth import get_user_model
user = get_user_model()



class resultAdminForm(forms.ModelForm):
    class Meta:
        model = results
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(resultAdminForm, self).__init__(*args, **kwargs)
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
            self.fields['player_mostboundaries'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostrun'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostwicktect'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostsixs'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))


class questionAdminForm(forms.ModelForm):
    class Meta:
        model = question
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(questionAdminForm, self).__init__(*args, **kwargs)
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
            self.fields['player_mostboundaries'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostrun'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostwicktect'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostsixs'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))

class questionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = ["winner", "tosswinner", "player_mostboundaries",
                  "player_mostsixs", "player_mostwicktect", "player_mostrun", "player_mom"]
        # fields = "__all__"
        labels = {
            "winner": "Select winner team for today's Ipl match." ,
            "tosswinner": "Who will win the toss?", 
            "player_mostboundaries":"Which player will hit most number of boundaries?",
            "player_mostsixs":"Which player will hit the most number of sixes?",
            "player_mostwicktect":"Which player will take the most wickets?",
            "player_mostrun":" Which player will score most runs?", 
            "player_mom":"Who will man of the match?",
        }

    def __init__(self, *args, **kwargs):
        super(questionForm, self).__init__(*args, **kwargs)

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
            self.fields['player_mostboundaries'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostrun'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostwicktect'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))
            self.fields['player_mostsixs'].queryset = iplplayer.objects.filter(
                Q(Teamname=pk1) | Q(Teamname=pk2))

