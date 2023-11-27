from django.contrib import admin
from .models import Artist, Album, Song

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]

class ArtistAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album')
    list_filter = ['album__title']
    search_fields = ('title', 'album__title', 'artist__name')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

# Register your models here.
