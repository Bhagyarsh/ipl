from django.shortcuts import render,redirect
from .forms import questionForm
from .models import question
from accounts.models import Player
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
user = get_user_model()
@login_required
def questionform(request):
    instance = get_object_or_404(question, id=5)
    print(instance)
    form = questionForm(request.POST or None,instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'registration/signup.html',{"form":form})