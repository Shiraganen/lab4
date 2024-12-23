from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_athlete, name='add_athlete'),
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.list_files, name='list_files'),
    path('upload/', views.upload_file, name='upload'),
]

