from django.db import models
from django.db.models.signals import pre_save,post_save

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
        ("RCB","Royal Challengers Bangalore"),
        ("SRH","Sunrisers Hyderabad	")]
class iplplayer(models.Model):
    Teamname = models.ForeignKey(to="IPLTeam" , on_delete=models.CASCADE,related_name="team")  
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
    logo = models.ImageField(null=True,upload_to='media/Team_logo/',blank=True)
    def __str__(self):              
        return self.Teamname





def IPLTeam_pre_save_receiver(sender, instance, *args, **kwargs):
    image_path = "Team_logo/" +  str(instance.Teamname) +".png"
    instance.logo = image_path
    
pre_save.connect(IPLTeam_pre_save_receiver, sender=IPLTeam)
