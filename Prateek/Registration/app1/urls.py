from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', views.LogoutPage, name='logout'),
]
