
from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','email','phone','designation','instagram','facebook','linkedin','twitter', 'image']
