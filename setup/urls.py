from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('usuarios/', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
