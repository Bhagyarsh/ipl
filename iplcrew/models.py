from django.db import models

# Create your models here.
choices=[("bat", "Batsman"),
        ("Bwl","Bowler"),
        ("WKB","Wicket keeper"),
        ("All","All rounder ")]
        
choices_team=[("CSK", "Chennai Super Kings"),
        ("DC","Delhi Capitals"),
        ("KX1P","Kings XI Punjab"),
        ("KKR","Kolkata Knight Riders"),
        ("RR","Rajasthan Royals"),
        ("MI","Mumbai Indians"),
        ("RBC","Royal Challengers Bangalore"),
        ("SRH","Sunrisers Hyderabad	")]
class iplplayer(models.Model):
    Teamname = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE)  
    name = models.CharField(max_length=120)
    player_type = models.CharField(choices=choices,max_length=120)

    def __str__(self):              
        return self.name


class ipletable(models.Model):
    Teamname = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE)  
    m =  models.IntegerField(default=0)
    l =  models.IntegerField(default=0)
    nrr =  models.FloatField(default=0.0)
    point =  models.IntegerField(default=0)

class IPLTeam(models.Model):
    Teamname = models.CharField(max_length = 120,choices=choices_team)
    def __str__(self):              
        return self.Teamname

class match(models.Model):
    team_1 = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE,related_name="team_1")
    team_2 = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE,related_name="team_2")
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    starttime = models.TimeField()
    def __str__(self):              
        return "{} vs {}".format(self.team_1,self.team_2)

class result(models.Model):
    toss = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE,related_name="tosswinner")
    match = models.ForeignKey(to="match" , on_delete=models.CASCADE,related_name="match")
    man_of_the_match = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE,related_name="mom")
    team = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE,related_name="winner")
    sixer_of_the_match =  models.ForeignKey(to=iplplayer,on_delete=models.CASCADE
                                ,related_name="sixer_man")
    fourer_of_the_match =  models.ForeignKey(to=iplplayer,on_delete=models.CASCADE
                                ,related_name="fourer_man")
    wikecter_of_the_match =  models.ForeignKey(to=iplplayer,on_delete=models.CASCADE
                                    ,related_name="wikecter_man")
