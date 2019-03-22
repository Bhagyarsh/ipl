from django.contrib import admin
from django.urls import path,include
from .views import  questionform
app_name = 'qaformmatch'
urlpatterns = [
    path('form/',questionform),
]
