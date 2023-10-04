from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer


class BookingBaseView:
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingListCreateView(BookingBaseView, generics.ListCreateAPIView):
    pass


class BookingDetailView(BookingBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass

