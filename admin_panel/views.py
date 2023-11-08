from datetime import date

from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from admin_panel.permission import IsManagerOrCounterUser
from tour_package.models import TourPackage
from tour_package.views import TourPackageBaseView
from rest_framework.permissions import IsAuthenticated


class TourPackageListCreateView(TourPackageBaseView, ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticated, IsManagerOrCounterUser]
    search_fields = ['name', 'description', 'location']

    def get_queryset(self):
        queryset = TourPackage.objects.all()
        is_active = self.request.query_params.get('is_active', 'false').lower() == 'true'
        start_date = self.request.query_params.get('start_date', date.today())
        end_date = self.request.query_params.get('end_date', None)
        queryset = queryset.filter(start_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)
        if is_active:
            queryset = queryset.filter(is_active=is_active)
        queryset = queryset.order_by('-id')
        return queryset


class TourPackageDetailView(TourPackageBaseView, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsManagerOrCounterUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Successfully deleted"}, status=status.HTTP_200_OK)

