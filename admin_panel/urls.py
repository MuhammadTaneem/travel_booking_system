from django.urls import path
from . import views


app_name = 'admin_panel'
urlpatterns = [
    path('tour/', views.TourPackageListCreateView.as_view(), name='tour-package-list-create'),
    path('tour/<int:pk>/', views.TourPackageDetailView.as_view(), name='tour-package-detail'),
]