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
            'location',
            'duration',
            'policy',
            'created_at',
            'last_edited',
        ]

    def perform_update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(partial=True)
