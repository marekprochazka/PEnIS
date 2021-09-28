from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from sleepover_form.models import SleepoverRequest
from sleepover_form.serializers.sleepover_request import SleepoverRequestSerializer, SleepoverRequestListSerializer, \
    SleepoverRequestUpdateSerializer


class SleepoverRequestListView(ListAPIView):
    serializer_class = SleepoverRequestListSerializer
    queryset = SleepoverRequest.objects.all()


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
