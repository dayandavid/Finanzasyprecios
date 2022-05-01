import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", include('main.urls')),

    path('admin/', admin.site.urls),
    
    # Django Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Administración del Sitio"  
admin.site.site_title  =  "Administración del Sitio"
admin.site.index_title  =  "Administración"
