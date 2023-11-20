from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', HomePageView.as_view()),
    re_path(r'^$', include('Template_home_page_view.urls')),
    # path('', include('Template_home_page_view.urls')),
    path('admin/', include('admin_panel.urls')),
    path('tour/', include('tour_package.urls')),
    path('booking/', include('booking.urls')),
    path('auth/', include('tauth.urls')),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
