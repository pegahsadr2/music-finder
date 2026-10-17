from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="search"),
    path("play/<int:song_id>/", views.play_song, name="play_song"),
    path("rescan/", views.rescan, name="rescan"),
    
]