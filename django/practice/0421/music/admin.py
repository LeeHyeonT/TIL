from django.contrib import admin
from .models import Music, Artist
# Register your models here.

class MusicAdmin(admin.ModelAdmin):
    list_dispay = ('pk', 'artist', 'title',)

admin.site.register(Music, MusicAdmin)
admin.site.register(Artist)
