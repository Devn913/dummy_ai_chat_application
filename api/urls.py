from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('chat/', views.ChatView.as_view()),
    path('tokens/', views.TokenBalance.as_view()),


]
