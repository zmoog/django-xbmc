from django.views.generic import DetailView, ListView

from .models import Actors, Movie


class MovieList(ListView):
    model = Movie
    context_object_name = 'movie_list'
    paginate_by = 20


class MovieDetail(DetailView):
    model = Movie


class ActorDetail(DetailView):
	model = Actors
	context_object_name = 'actor'