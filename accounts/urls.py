# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('register/',views.signup,name="register"),
    path('leaderboards/',views.leaderboards,name="leaderboards")
]
