from django.urls import path

from sleepover_form.views.sleepover_request import SleepoverRequestListView, SleepoverRequestCreateView, \
    SleepoverRequestDestroyView, SleepoverRequestAcceptStatusUpdateView
from sleepover_form.views.types import TypeCoitusProbabilityListView

app_name = 'sleepover_form'

urlpatterns = [
    path('list', SleepoverRequestListView.as_view(), name='list'),
    path('create', SleepoverRequestCreateView.as_view(), name='create'),
    path('destroy/<str:pk>', SleepoverRequestDestroyView.as_view(), name='destroy'),
    path('coitus-probabilities/list', TypeCoitusProbabilityListView.as_view(), name='coitus_probabilities_list'),
    path('accept-status/<str:pk>', SleepoverRequestAcceptStatusUpdateView.as_view(), name='accept_status_update'),
]
