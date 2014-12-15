from django.views.generic import DetailView, ListView
from .models import Movie


class MovieList(ListView):
    model = Movie
    context_object_name = 'movie_list'
    paginate_by = 20


class MovieDetail(DetailView):
    model = Movie