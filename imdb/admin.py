from django.contrib import admin

from .models import Movie, Genre


# Class to create CRUD and Filter table for Movie Model in Admin
class MovieAdmin(admin.ModelAdmin):
    # Fields to be shown
    fields = ['name', 'popularity', 'imdb_score', 'director', 'genres']

    # display order
    list_display = ('name', 'popularity', 'imdb_score', 'director', 'get_genres')

    # filters for the listing. Can be updated to include more fields.
    list_filter = ['director', 'genres']

    # searchable fields list
    search_fields = ['name', 'popularity', 'imdb_score', 'director', 'genres']


# Class to create CRUD and Filter table for Genre Model in Admin
class GenreAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
