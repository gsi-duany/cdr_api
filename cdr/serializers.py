from .models import Cdr
from rest_framework import serializers

class CdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cdr
        fields = '__all__'