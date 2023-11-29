from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('sign-up/', views.sign_up, name = 'signup'),
    path('login/', views.login_user, name='login'),   
]