from rest_framework import serializers
from .models import TourPackage


class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = [
            'id',
            'name',
            'description',
            'image_1',
            'image_2',
            'image_3',
            'price',
            'discount',
            'start_date',
            'end_date',
            'daily_limit',
            'is_active',
            'is_paid',
            'location',
            'duration',
            'policy',
            'created_at',
            'last_edited',
        ]
