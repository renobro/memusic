from django.urls import path
from . import views

app_name = 'song'

urlpatterns = [

    path('', views.music_list, name='music_list'),
    path('songs/', views.song_list, name='song_list'),
    path('albums/', views.album_list, name='album_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),

]
