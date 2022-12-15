from rest_framework import serializers
from .models import Moto

# Register your models here.

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = (
            "id",
            "reference",
            "trademark",
            "model",
            "price",
            "image",
            "supplier",
)
