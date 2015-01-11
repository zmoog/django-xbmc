from django.conf.urls import url

from .views import ActorDetail, MovieDetail, MovieList


urlpatterns = (

    url(r'^movies/$', MovieList.as_view(), name='movie-list'),
    url(r'^movies/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie-detail'),
    
    url(r'^actors/(?P<pk>\d+)/$', ActorDetail.as_view(), name='actor-detail'),
)