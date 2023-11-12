from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking.models import Booking
from booking.serializers import BookingSerializer
from traveler.enum import BookingStatus


class BookingBaseView:
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_booking(request):
#     import pdb;pdb.set_trace()


class BookingListCreateView(BookingBaseView, generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Booking.objects.filter(customer__id=self.request.user.id)
        queryset = queryset.order_by('-id')
        return queryset

    def perform_create(self, serializer):
        serializer.save(status=BookingStatus.up_coming, customer=self.request.user)


class BookingDetailView(BookingBaseView, generics.RetrieveAPIView):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def booking_cancel(request):
    booking_id = request.data.get('id', None)
    if booking_id is None:
        return Response({'message': 'Booking id is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({'message': 'Booking not found'}, status=status.HTTP_400_BAD_REQUEST)
    if booking.customer == request.user:
        try:
            booking.status = BookingStatus.canceled
            booking.save()
            return Response({"detail": "Booking Cancel successfully."}, status=status.HTTP_200_OK)

        except:
            return Response({"detail": "Internal Server Error."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Your are not permitted to cancel this booking"}, status=status.HTTP_400_BAD_REQUEST)


def booking_paid(self):
    pass
