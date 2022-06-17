from rest_framework import serializers
from .models import Cattle


class CattleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at")
        model = Cattle