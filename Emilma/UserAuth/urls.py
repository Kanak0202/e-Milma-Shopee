from django.urls import path
from UserAuth import views

urlpatterns = [
    path("login", views.loginUser, name='login'),
    path("register", views.register, name='register'),
    path("logout", views.logoutUser, name='logout'),
]