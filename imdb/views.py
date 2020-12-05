from django.http import HttpResponse
from django.views import generic
from imdb.models import Movie
from .filters import MovieFilter
from django.shortcuts import render


# search view for movie listings
def search(request):
    movie_list = Movie.objects.all()
    user_filter = MovieFilter(request.GET, queryset=movie_list)
    return render(request, 'imdb/movie_list.html', {'filter': user_filter})
