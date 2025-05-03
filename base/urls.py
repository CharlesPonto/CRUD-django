from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-player/', views.createPlayer, name='create-player'),
    path('update-player', views.updatePlayer, name='update-player'),
    path('detete-playe', views.deletePlayer, name='delete-player'),
]
