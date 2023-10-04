from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'user_type',
            'phone_number',
            'is_active',
            'is_staff',
            'date_joined',
        ]
