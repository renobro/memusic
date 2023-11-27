from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='album_covers/')

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='songs/')


class DJUpload(models.Model):
    title = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    zip_file = models.FileField(upload_to='dj_uploads/')
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title

# Create your models here.
