from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from sleepover_form.models import SleepoverRequest
from sleepover_form.serializers.sleepover_request import SleepoverRequestSerializer, SleepoverRequestListSerializer


class SleepoverRequestListView(ListAPIView):
    serializer_class = SleepoverRequestListSerializer
    queryset = SleepoverRequest.objects.all()


class SleepoverRequestCreateView(CreateAPIView):
    serializer_class = SleepoverRequestSerializer


class SleepoverRequestDestroyView(DestroyAPIView):
    queryset = SleepoverRequest.objects.all()
