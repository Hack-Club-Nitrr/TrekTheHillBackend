
from rest_framework import serializers
from .models import Judge


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = ['name','email','designation','linkedin','github','image','preference']
