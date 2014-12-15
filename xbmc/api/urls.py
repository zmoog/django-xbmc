from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from showcase.models import Movie


# Serializers define the API representation.
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('idmovie', 'c00', 'c01', 'c05', 'c06', 'c07', 'c08', 'c12', 'c14', 'c15', 'c21', )

# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]