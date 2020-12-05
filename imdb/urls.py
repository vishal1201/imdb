from django.conf.urls import url
from django.urls import path
from django_filters.views import FilterView

from . import views
from .filters import MovieFilter

app_name = 'imdb'
urlpatterns = [
    url('', FilterView.as_view(filterset_class=MovieFilter,
                                         template_name='imdb/movie_list.html'))
]
