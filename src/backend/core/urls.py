from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('test', TemplateView.as_view(template_name='index.html'), name='test')
]
