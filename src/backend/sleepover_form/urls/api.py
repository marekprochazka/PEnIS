from django.urls import path

from sleepover_form.views.sleepover_request import SleepoverRequestListView, SleepoverRequestCreateView, \
    SleepoverRequestDestroyView

app_name = 'sleepover_form'

urlpatterns = [
    path('list', SleepoverRequestListView.as_view(), name='list'),
    path('create', SleepoverRequestCreateView.as_view(), name='create'),
    path('destroy/<str:pk>', SleepoverRequestDestroyView.as_view(), name='destroy'),
]
