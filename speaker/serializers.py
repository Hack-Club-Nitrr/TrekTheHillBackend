
from rest_framework import serializers
from .models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ['name','email','designation','linkedin','github','image','role','preference']
