from rest_framework.generics import ListAPIView

from shopping.models.types import TypeUrgency
from shopping.serializers.types import TypeUrgencySerializer


class TypeUrgencyListView(ListAPIView):
    serializer_class = TypeUrgencySerializer
    queryset = TypeUrgency.objects.all()