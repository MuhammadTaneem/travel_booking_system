from datetime import date
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from tour_package.models import TourPackage
from tour_package.serializers import TourPackageSerializer


class TourPackageBaseView:
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer


class TourPackageListCreateView(TourPackageBaseView, ListAPIView):
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'location']

    def get_queryset(self):
        queryset = TourPackage.objects.filter(is_active=True)
        start_date = self.request.query_params.get('start_date', date.today())
        end_date = self.request.query_params.get('end_date', None)
        queryset = queryset.filter(start_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)
        queryset = queryset.order_by('-id')
        return queryset


class TourPackageDetailView(TourPackageBaseView, RetrieveAPIView):
    pass
