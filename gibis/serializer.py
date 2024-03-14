from rest_framework import routers, serializers, viewsets
from gibis.models import *

class GibiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gibi
        fields = ['id', 'name', 'authors']

# ViewSets define the view behavior.
class GibiViewSet(viewsets.ModelViewSet):
    queryset = Gibi.objects.all()
    serializer_class = GibiSerializer