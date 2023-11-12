from django.urls import path
from . import views

urlpatterns = [
    # path('', views.create_booking, name='booking-list-create'),
    path('', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('cancel/', views.booking_cancel, name='booking-cancel'),
]