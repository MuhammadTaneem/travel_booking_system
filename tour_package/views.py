from django.utils import timezone
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination

# from booking.models import Booking
from .models import TourPackage
from .serializers import TourPackageSerializer


class TourPackageBaseView:
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer


class TourPackageListCreateView(TourPackageBaseView, ListAPIView):
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'location']

    def get_queryset(self):
        return TourPackage.objects.filter(start_date__gte=timezone.now().date(), is_active=True)


class TourPackageDetailView(TourPackageBaseView, RetrieveAPIView):
    pass
