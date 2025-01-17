from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import Login, Logout
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Documentation API",
      default_version='v1',
      description="Docuemntacion publica de api modulo 2 - Proyecto de Grado",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dehurtado@unbosque.edu.co"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #Configuracion para documentacion swagger (repath)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('usuario/', include('users.api.urls')),
    path('vehiculo/', include('vehiculosApp.api.urls')),
    path('parking/', include('parking.api.urls')),
    path('docs/', include_docs_urls(title='Fast Pay')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
