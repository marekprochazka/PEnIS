from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from sleepover_form.models import SleepoverRequest
from sleepover_form.serializers.sleepover_request import SleepoverRequestSerializer, SleepoverRequestListSerializer, \
    SleepoverRequestUpdateSerializer
from datetime import date
from django.db.models import Q


class SleepoverRequestListView(ListAPIView):
    serializer_class = SleepoverRequestListSerializer

    def get_queryset(self):
        today = date.today()
        return SleepoverRequest.objects.filter(
            Q(sleepover_date_from__range=[today, '3000-01-01']) | Q(sleepover_date_from__isnull=True))
        # return SleepoverRequest.objects.all()


class SleepoverRequestCreateView(CreateAPIView):
    serializer_class = SleepoverRequestUpdateSerializer


class SleepoverRequestDestroyView(DestroyAPIView):
    queryset = SleepoverRequest.objects.all()


class SleepoverRequestAcceptStatusUpdateView(APIView):
    def post(self, request, pk):
        sleepover_request = SleepoverRequest.objects.get(id=pk)
        accept_status = request.data.get('accept_status', None)
        if accept_status is not None and type(accept_status) == bool:
            sleepover_request.accepted = accept_status
            sleepover_request.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
