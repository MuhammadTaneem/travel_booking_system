from django.utils import timezone
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from tour_package.views import TourPackageBaseView
from tour_package.models import TourPackage


class TourPackageListCreateView(TourPackageBaseView, ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'location']

    def get_queryset(self):
        if self.request.user.user_type == 'manager' or self.request.user.user_type == 'counter':
            queryset = TourPackage.objects.all()
            is_active = self.request.query_params.get('is_active', 'false').lower() == 'true'
            show_previous = self.request.query_params.get('show_previous', 'false').lower() == 'true'
            if not show_previous:
                queryset = TourPackage.objects.filter(start_date__gte=timezone.now().date())
            if is_active:
                queryset = queryset.filter(is_active=is_active)
            return queryset
        else:
            return TourPackage.objects.none


class TourPackageDetailView(TourPackageBaseView, RetrieveUpdateDestroyAPIView):
    pass
