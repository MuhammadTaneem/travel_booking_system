from django.urls import path
from . import views

urlpatterns = [
    path('', views.TourPackageListCreateView.as_view(), name='tour-package-list-create'),
    path('<int:pk>/', views.TourPackageDetailView.as_view(), name='tour-package-detail'),
]