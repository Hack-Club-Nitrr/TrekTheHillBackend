from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamSerializer
from .models import Team

class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


def index(request):
    return render(request, 'index.html')
