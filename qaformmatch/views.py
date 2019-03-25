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

@login_required
def questionform(request):

    player_user = user.objects.get(email=request.user)
    player = Player.objects.get(User=player_user.pk)
    m1 = match.objects.filter(startdate = datetime.now().date())[0]
    instance = question.objects.get(match=m1)
    if instance:
        form = questionForm(request.POST or None, instance=instance)
        form.initial['Player'] = player
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect('/')
        return render(request, 'questions.html', {"form": form,"qs":m1})



