from rest_framework import serializers
from .models import Booking
# from custom_users.serializers import CustomUserSerializer
from tour_package.serializers import TourPackageSerializer


class BookingSerializer(serializers.ModelSerializer):
    # customer = CustomUserSerializer()
    tour_package = TourPackageSerializer()

    class Meta:
        model = Booking
        fields = [
            'id',
            'customer',
            'tour_package',
            'date',
            'is_paid',
            'no_of_person',
            'created_at',
            'last_edited',
        ]
