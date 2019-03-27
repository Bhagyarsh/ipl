from django.shortcuts import render,redirect
from .forms import RegisterFormSession
from datetime import datetime
from .models import Player
from qaformmatch.models import match
def home(request):
    now = datetime.now()
    t_day = now.date()
    t_time = now.time()
    m1 = match.objects.filter(startdate=t_day)
    mt = m1.count()
    return render(request,'nomatch.html')
    if mt != 0 :
        print(m1[0].starttime)
        print(type(m1[0].starttime))
        print(m1.count())
        return render(request,'home.html',{"qs":m1[0]})
    else :
        return render(request,'nomatch.html')

def signup(request):
    if request.method == "POST":
        form = RegisterFormSession(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')

    else:
        form = RegisterFormSession()
    return render(request,'registration/signup.html',{"form":form})


def leaderboards(request):
	qs = Player.objects.all()
	return render(request, 'leaderboards.html',{"qs":qs})