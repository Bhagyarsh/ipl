from django.shortcuts import render,redirect
from .forms import questionForm
# Create your views here.

def questionform(request):
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = questionForm()
    return render(request,'registration/signup.html',{"form":form})