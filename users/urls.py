from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("profile/change-password/", views.change_password, name="change_password"),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('toggle_dark_mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]