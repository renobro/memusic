from django.shortcuts import render, get_object_or_404
from .models import Song, Album, Artist





def music_list(request):
    songs = Song.objects.all()
    return render(request, 'music_list.html', {'songs': songs})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})




def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})

# Create your views here.
