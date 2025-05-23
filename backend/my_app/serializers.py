from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'image',
            'compressed_url',
            'email',
            'status'
        ]
        read_only_fields = ['id', 'status']
        

