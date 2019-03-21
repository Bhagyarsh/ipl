from django.db import models
from iplcrew.models import match,IPLTeam,iplplayer
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
# 1. Who will win the toss?
# 2. Select winner team for today's Ipl match.
# 3. Which player will score most runs?
# 4. Which player will take the most wickets?
# 5. Which player will hit the most number of sixes?
# 6. Which player will hit most number of boundaries?
# 7. Who will man of the match?
class Player(models.Model):
    User = models.ForeignKey(to=User,on_delete=models.CASCADE)
    points = models.IntegerField()
class question_toss(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Who will win the toss?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    tosswinner = models.ForeignKey(to=IPLTeam,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class question_winner(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Select winner team for today's Ipl match.")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    winner = models.ForeignKey(to=IPLTeam,on_delete=models.CASCADE)

    def __str__(self):
        return self.question
class question_mostrun(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Which player will score most runs?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    player = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
class question_mostsixes(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Which player will hit the most number of sixes?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    player = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE)

    def __str__(self):
        return self.question
class question_mostwickets(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Which player will take the most wickets?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    player = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE)

    def __str__(self):
        return self.question
class question_mostboundaries(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Which player will hit most number of boundaries?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    player = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class question_mom(models.Model):
    user = models.ForeignKey(to=Player,on_delete=models.CASCADE)
    question = models.TextField(default="Who will man of the match?")
    match = models.ForeignKey(to=match,on_delete=models.CASCADE)
    player = models.ForeignKey(to=iplplayer,on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return self.question