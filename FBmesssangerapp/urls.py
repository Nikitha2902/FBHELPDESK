from django.urls import path,include
from .views import *
from django.contrib import admin
from django.urls import path
from FBmesssangerapp import views

urlpatterns = [
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('',views.SignupPage,name='signup'),
    path('fbconnect', views.LoginPage, name='fbconnect'),
    path('chat/', views.chat, name='chat'),
]