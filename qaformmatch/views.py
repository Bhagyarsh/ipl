from django.shortcuts import render, redirect
from .forms import questionForm
from .models import question,match
from django import forms
from accounts.models import Player
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
user = get_user_model()
from datetime import datetime 
from datetime import timedelta
@login_required
def questionform(request):
    player_user = user.objects.get(email=request.user)
    player = Player.objects.get(User=player_user.pk)
    m1 = match.objects.filter(startdate = datetime.now().date())
    now_time = datetime.now().time()
    num = m1.count()
    if int(num)>0:
        if int(num) == 1:
            starttime = (m1[0].starttime) 
            dif = timedelta(hours=starttime.hour,minutes=starttime.minute) - timedelta(hours=1,minutes=45)
            today_time = datetime.today().time() 
            dif =  dif -timedelta(hours=today_time.hour,minutes=today_time.minute) 
            if (dif.days) < 0 :
                return render(request, 'home.html',{"qs":m1[0]})
    instance = question.objects.get(match=m1[0])
    if instance:
        form = questionForm(request.POST or None, instance=instance)
        form.initial['Player'] = player
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect('/')
        return render(request, 'questions.html', {"form": form,"qs":m1[0]})



