from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta: 
        model = super
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1