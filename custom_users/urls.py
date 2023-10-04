from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.CustomUserListCreateView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', views.CustomUserDetailView.as_view(), name='user-detail'),
]