from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create-room/', views.create_room,name='create_room'),
    path('login/', views.login_page,name='login'),
    path('profile/', views.profile_page,name='profile'),
    path('edit-user/', views.edit_userPage,name='edit-user'),
    path('register/', views.signup_page,name='register'),
    path('logout/', views.logout_page,name='logout'),
    path('<str:topic_room>/',views.home, name='topic-room'),
    path('room/<str:pk>',views.room,name='room'),
]