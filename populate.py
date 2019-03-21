import os 
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipl_green.settings')
import django
django.setup()
from iplcrew.models import iplplayer,IPLTeam

def add_player(row):
    print(row)
    name ,role , team = row
    team = IPLTeam.objects.get_or_create(Teamname=team)[0]
    t = iplplayer.objects.get_or_create(Teamname =team,name=name,player_type=role)[0]
    t.save()
    return t


with open('iplplayer - Sheet1.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile)
     for row in spamreader:
        add_player(row)

            