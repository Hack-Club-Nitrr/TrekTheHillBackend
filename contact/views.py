from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact

class TeamView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()



