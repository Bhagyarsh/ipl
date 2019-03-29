from django.db import models
from django import forms
from iplcrew.models import IPLTeam, iplplayer
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save,post_save

User = get_user_model()




Player = "accounts.Player"
class match(models.Model):
    team_1 = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="mteam_1")
    team_2 = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="mteam_2")
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    starttime = models.TimeField()

    def __str__(self):
        return "{} vs {}".format(self.team_1, self.team_2)


class question(models.Model):
    match = models.ForeignKey(to=match, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    filled = models.BooleanField(default=False,null=True)
    Player = models.ForeignKey(to=Player, on_delete=models.CASCADE, null=True)
    winner = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="P_teamwinner", null=True)
    tosswinner = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="P_tosswinner", null=True)
    player_mom = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="P_momr", null=True)
    player_mostboundaries = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="P_mostboundaries", null=True)
    player_mostwicktect = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="P_mostwicktect", null=True)
    player_mostrun = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="P_mostrun", null=True)
    player_mostsixs = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="P_mostsixs", null=True)
    points =  models.IntegerField(default=0,blank=True,null=True)
    # def __str__(self):
    #     return self.match


class results(models.Model):
    match = models.ForeignKey(to=match, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    winner = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="R_teamwinner", null=True)
    tosswinner = models.ForeignKey(
        to=IPLTeam, on_delete=models.CASCADE, related_name="R_tosswinner", null=True)
    player_mom = models.ForeignKey(
        to=iplplayer, on_delete=models.CASCADE, related_name="R_momr", null=True)
    player_mostboundaries = models.ManyToManyField(
        to=iplplayer, related_name="R_mostboundaries")
    player_mostwicktect = models.ManyToManyField(
        to=iplplayer,related_name="R_mostwicktect")
    player_mostrun = models.ManyToManyField(
        to=iplplayer, related_name="R_mostrun")
    player_mostsixs = models.ManyToManyField(
        to=iplplayer, related_name="R_mostsixs")
    done = models.BooleanField(null=True,default=False)
    # def __str__(self):
    #     return self.match


def match_pre_save_receiver(sender, instance, *args, **kwargs):
    pass

def match_post_save_receiver(sender, instance,created, *args, **kwargs):
    print(instance)
    if created:
        from accounts.models import Player
        Players = Player.objects.all()
        print(Players)
        for player in Players.iterator():
            print(player.pk)
            q = question.objects.create(
                match=instance, team1=instance.team_1,Player=player, team2=instance.team_2)
        r = results.objects.create(
                match=instance, team1=instance.team_1, team2=instance.team_2)

def result_post_save_receiver(sender, instance,created, *args, **kwargs):

    if  instance.done and instance.done != None:
        match = instance.match 
        questions = question.objects.filter(match=match)

        for que in questions:
            print(que)
            print(que.winner)
            points = 0
            player = que.Player.pk
            print("---------------------------")
            points = 0
            winner = que.winner
            tosswinner = que.tosswinner
            player_mostboundaries = que.player_mostboundaries
            player_mostsixs = que.player_mostsixs
            player_mostwicktect = que.player_mostwicktect
            player_mostrun = que.player_mostrun
            player_mom = que.player_mom
            
            if winner == instance.winner:
                print(winner,instance.winner)   
                points+=2
            if tosswinner == instance.tosswinner:
                print(tosswinner,instance.tosswinner)   
                points+=2
            if str(player_mostboundaries) in [ (i.name) for i in instance.player_mostboundaries.all()] :
                print(player_mostboundaries,[ (i.name) for i in instance.player_mostboundaries.all()] )
                points+=2
            if str(player_mostsixs) in [ (i.name) for i in instance.player_mostsixs.all()] :
                print(player_mostsixs,[ (i.name) for i in instance.player_mostsixs.all()] )
                points+=2
            print([ i.name for i in instance.player_mostwicktect.all()])
            if str(player_mostwicktect) in [ (i.name) for i in instance.player_mostwicktect.all()] :
                print(player_mostwicktect,[ (i.name) for i in instance.player_mostwicktect.all()] )
                points+=2
            if str(player_mostrun) in [ (i.name) for i in instance.player_mostrun.all()] :
                print(player_mostrun,[ (i.name) for i in instance.player_mostrun.all()] )
                points+=2
            if player_mom == instance.player_mom:
                points+=2
            que.points = points
            from accounts.models import Player
            p = Player.objects.get(pk=str(player))
            print(p)
            pointsx = int(p.points)
            pointsx += points
            questions = question.objects.filter(match=match).update(points=str(points))
            Player.objects.filter(pk=str(player)).update(points=str(pointsx))
            print(points)
pre_save.connect(match_pre_save_receiver, sender=match)
post_save.connect(match_post_save_receiver, sender=match)
post_save.connect(result_post_save_receiver, sender=results)
