from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    """Serializer for Quote object"""
    class Meta:
        model = Quote
        fields = '__all__'