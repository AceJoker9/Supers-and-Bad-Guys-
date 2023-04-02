from rest_framework import serializers
from .models import Super_type

class super_typeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Super_type
        fields = ['type']

        