# Generated by Django 2.1.7 on 2019-03-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iplcrew', '0001_initial'),
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('starttime', models.TimeField()),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mteam_1', to='iplcrew.IPLTeam')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mteam_2', to='iplcrew.IPLTeam')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=250)),
                ('team2', models.CharField(max_length=250)),
                ('Player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Player')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qaformmatch.match')),
                ('player_mom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_momr', to='iplcrew.iplplayer')),
                ('player_mostboundaries', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_mostboundaries', to='iplcrew.iplplayer')),
                ('player_mostrun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_mostrun', to='iplcrew.iplplayer')),
                ('player_mostsixs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_mostsixs', to='iplcrew.iplplayer')),
                ('player_mostwicktect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_mostwicktect', to='iplcrew.iplplayer')),
                ('tosswinner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_tosswinner', to='iplcrew.IPLTeam')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_teamwinner', to='iplcrew.IPLTeam')),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=250)),
                ('team2', models.CharField(max_length=250)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qaformmatch.match')),
                ('player_mom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_momr', to='iplcrew.iplplayer')),
                ('player_mostboundaries', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_mostboundaries', to='iplcrew.iplplayer')),
                ('player_mostrun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_mostrun', to='iplcrew.iplplayer')),
                ('player_mostsixs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_mostsixs', to='iplcrew.iplplayer')),
                ('player_mostwicktect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_mostwicktect', to='iplcrew.iplplayer')),
                ('tosswinner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_tosswinner', to='iplcrew.IPLTeam')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='R_teamwinner', to='iplcrew.IPLTeam')),
            ],
        ),
    ]
