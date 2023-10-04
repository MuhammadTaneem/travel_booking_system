from django.urls import path
from . import views

urlpatterns = [
    path('tour-package/', views.TourPackageListCreateView.as_view(), name='tour-package-list-create'),
    path('tour-package/<int:pk>/', views.TourPackageDetailView.as_view(), name='tour-package-detail'),
]