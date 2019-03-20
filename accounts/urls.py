# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
]
