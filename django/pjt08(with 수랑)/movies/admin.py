from django.contrib import admin
from .models import Actor, Movie, Review

# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'actors', 'title', 'overview', 'release_date', 'poster_path',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'movie',)

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Review)