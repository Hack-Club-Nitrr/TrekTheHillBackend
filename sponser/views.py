from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SponserSerializer
from .models import Sponser

class SponserView(viewsets.ModelViewSet):
    serializer_class = SponserSerializer
    queryset = Sponser.objects.all()



