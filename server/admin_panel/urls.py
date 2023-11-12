from django.urls import path
from admin_panel.views import *


app_name = 'admin_panel'
urlpatterns = [
    path('tour/', TourPackageListCreateView.as_view(), name='tour-package-list-create'),
    path('tour/<int:pk>/', TourPackageDetailView.as_view(), name='tour-package-detail'),
    # path('tour/', views.TourPackageListCreateView.as_view(), name='tour-package-list-create'),
]