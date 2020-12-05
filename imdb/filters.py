import django_filters
from django import forms

from .models import Movie, Genre


# Class to implement Movie Filter in users access mode.
class MovieFilter(django_filters.FilterSet):
    # a 'contains in' name type search for movie name
    name = django_filters.CharFilter(lookup_expr='icontains')
    # a 'contains in' name type search for director name
    director = django_filters.CharFilter(lookup_expr='icontains')
    # Checkbox style selection for genre based fileration
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Movie
        fields = ['name', 'director', 'imdb_score', 'popularity', 'genres']
