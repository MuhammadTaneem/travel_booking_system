from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_panel.urls')),
    path('tour/', include('tour_package.urls')),
    path('booking/', include('booking.urls')),
    path('auth/', include('tauth.urls')),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
