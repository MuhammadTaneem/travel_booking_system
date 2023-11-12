from datetime import date
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from admin_panel.permission import IsManagerOrCounterUser
from booking.models import Booking
from booking.views import BookingBaseView
from tour_package.models import TourPackage
from tour_package.views import TourPackageBaseView

from traveler.enum import BookingStatus


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


class BookingListCreateView(BookingBaseView, generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, IsManagerOrCounterUser]

    def get_queryset(self):
        queryset = Booking.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        package_id = self.request.query_params.get('package_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if customer_id:
            queryset = queryset.filter(customer=customer_id)

        if package_id:
            queryset = queryset.filter(tour_package=package_id)

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        queryset = queryset.order_by('-id')
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        booking_id = instance.id
        receiver_id = self.request.user.id
        amount = self.request.data.get('amount', None)
        is_paid = serializer.validated_data.get('is_paid')
        if is_paid:

            make_on_cash_booking_payment(booking_id, receiver_id, amount)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsManagerOrCounterUser])
def make_paid(request):
    booking_id = request.data.get('booking_id', None)
    receiver_id = request.user.id
    amount = request.data.get('amount', None)
    if not booking_id:
        return Response({"message": "Booking id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        booking = Booking.objects.get(booking_id)
        make_on_cash_booking_payment(booking_id, receiver_id, amount)
        booking.is_paid = True
        booking.save()
    except Booking.DoesNotExist:
        return Response({"message": "Invalid id, booking dos not exist"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsManagerOrCounterUser])
def cancel_booking(request):
    booking_id = request.data.get('booking_id', None)
    if not booking_id:
        return Response({"message": "Booking id is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        booking = Booking.objects.get(booking_id)
        booking.status = BookingStatus.canceled
        booking.save()
    except Booking.DoesNotExist:
        return Response({"message": "Invalid id, booking dos not exist"}, status=status.HTTP_400_BAD_REQUEST)


# change status by batch
# Replace with your actual enum import
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsManagerOrCounterUser])
def change_booking_status(request):
    try:

        booking_ids = request.data.get('booking_ids', [])
        new_status = request.data.get('new_status', '')
        bookings = Booking.objects.filter(id__in=booking_ids)

        if new_status not in [choice[0] for choice in BookingStatus.choices]:
            return Response({"message": "Invalid Status"}, status=status.HTTP_400_BAD_REQUEST)

        for booking in bookings:
            booking.status = new_status
            booking.save()
        return Response({"message": "Status updated successfully"}, status=status.HTTP_200_OK)
    except Booking.DoesNotExist:
        return Response({"message": "Ids list is empty"}, status=status.HTTP_400_BAD_REQUEST)


def make_on_cash_booking_payment(booking_id, receiver_id, amount):
    if amount is None:
        amount = Booking.objects.get(booking_id).tour_package.price

