from rest_framework.generics import ListAPIView

from sleepover_form.models import TypeCoitusProbability
from sleepover_form.serializers.types import TypeCoitusProbabilitySerializer


class TypeCoitusProbabilityListView(ListAPIView):
    serializer_class = TypeCoitusProbabilitySerializer
    queryset = TypeCoitusProbability.objects.all()
