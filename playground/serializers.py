from rest_framework import serializers
from .models import diagnose

class diagnoseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnose
        fields = ['id', 'create_date', 'images', 'labels']
