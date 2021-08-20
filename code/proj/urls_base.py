import notifications.urls
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('', include('switchblade_dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    if (
            settings.ACTUAL_ENV == "dev"
            and settings.DEBUG
            and settings.USE_SILK
            and "silk" in settings.INSTALLED_APPS
    ):
        urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
except ImportError:
    pass
