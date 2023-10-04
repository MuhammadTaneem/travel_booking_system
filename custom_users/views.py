from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserBaseView:
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListCreateView(CustomUserBaseView, generics.ListCreateAPIView):
    pass


class CustomUserDetailView(CustomUserBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass
