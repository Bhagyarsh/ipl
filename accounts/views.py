from django.shortcuts import render,redirect
from .forms import RegisterFormSession

from .models import Player

def home(request):
    return render(request,'home.html')

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
	qs = Player.objects.points(request.user)
	qs1 = Player.points
	print(qs1,'qs1')
	return render(request, 'leaderboards.html',{"qs":qs})