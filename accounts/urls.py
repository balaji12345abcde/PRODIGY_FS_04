from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path
urlpatterns=[
    path('signup/',signupview,name="signup"),
    path('login/',loginview,name="login"),
    path('logout/',logoutview,name="logout"),
    path("index", index, name="index"),
]