from rest_framework import serializers
from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'customer',
            'tour_package',
            'date',
            'status',
            'no_of_person',
            'created_at',
            'last_edited',
        ]

    def perform_update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(partial=True)
