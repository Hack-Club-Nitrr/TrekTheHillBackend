
from rest_framework import serializers
from .models import Sponser


class SponserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponser
        fields = ['name','link','image','category']
