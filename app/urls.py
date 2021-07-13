from django.urls import path

from app import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('projects/', views.projects, name="projects")
]
