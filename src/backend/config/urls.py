from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PEnIS API",
        default_version='0.1',
        description="Backend API for Flat Electronic Information System (PEnIS)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/core/', include('core.urls.api')),
    path('api/sleepover-form/', include('sleepover_form.urls.api')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('<path:resource>', TemplateView.as_view(template_name='index.html'), name='index_pathed'),
]
