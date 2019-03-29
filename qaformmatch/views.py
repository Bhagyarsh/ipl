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
    print(m1.count())
    if (m1.count() == 0 ):
        return render(request, 'notavailable.html')
    for i in m1:
        print(i)
    now_time = datetime.now().time()
    num = m1.count()
    m1_done = False
    if int(num)>0:
        if int(num) == 1:
            starttime = (m1[0].starttime) 
            dif = timedelta(hours=starttime.hour,minutes=starttime.minute) - timedelta(hours=0,minutes=45)
            today_time = datetime.today().time() 
            dif =  dif -timedelta(hours=today_time.hour,minutes=today_time.minute) 
            print("+++++")
            print(dif )
          

            if (dif.days) < 0 :
                m1_done = True
                return render(request, 'notavailable.html')
        if int(num) == 2:
            starttime = (m1[0].starttime) 
            dif = timedelta(hours=starttime.hour,minutes=starttime.minute) - timedelta(hours=0,minutes=45)
            today_time = datetime.today().time() 
            dif =  dif -timedelta(hours=today_time.hour,minutes=today_time.minute) 
            if (dif.days) < 0 :
                m1_done = True
                return render(request, 'notavailable.html')
            starttime = (m1[1].starttime) 
            dif = timedelta(hours=starttime.hour,minutes=starttime.minute) - timedelta(hours=0,minutes=45)
            today_time = datetime.today().time() 
            dif =  dif -timedelta(hours=today_time.hour,minutes=today_time.minute) 
            print("---------------")
            print(dif )
            

            if (dif.days) < 0 :
                return render(request, 'notavailable.html')
    instance = None
    if m1_done:
        if int(num) == 2:
            instance = question.objects.get(match=m1[1],Player=player)
            obj = m1[1]
        
    else :
        instance = question.objects.get(match=m1[0],Player=player)
        obj = m1[0]
    if instance:
        form = questionForm(request.POST or None, instance=instance)
        form.initial['Player'] = player
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return render(request, 'formredirect.html')
        return render(request, 'questions.html', {"form": form,"qs":obj})



