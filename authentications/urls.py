from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('home/', Home.as_view(), name='home'),
    path('register/', SignUpView2.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('pass/', ChangePassword.as_view(), name='ch_pass'),
    path('settings/', UserSettings.as_view(), name='settings'),
]
