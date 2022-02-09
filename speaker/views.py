from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SpeakerSerializer
from .models import Speaker

class SpeakerView(viewsets.ModelViewSet):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()



