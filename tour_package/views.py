from rest_framework import generics
from .models import TourPackage
from .serializers import TourPackageSerializer


class TourPackageBaseView:
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer


class TourPackageListCreateView(TourPackageBaseView, generics.ListCreateAPIView):
    pass


class TourPackageDetailView(TourPackageBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass
