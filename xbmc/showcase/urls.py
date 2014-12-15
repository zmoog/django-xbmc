from django.conf.urls import url
from .views import MovieDetail, MovieList

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='movie-list'),
    url(r'^(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie-detail'),
]