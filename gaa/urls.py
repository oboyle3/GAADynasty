from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("start-season/", views.start_season, name="start_season"),
]
