from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="start_page"),
    path('login/', views.login_page, name="login_page"),
    path('registration/', views.registration_page, name="registration_page"),
    path('main/', views.mainPage, name="dashboard"),
    path('addTask/', views.addTask, name="addTask"),
    path('updateTask/', views.updateTask, name="updateTask"),
    path('viewTask/', views.viewTask, name="viewTask"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate')
]