from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JudgeSerializer
from .models import Judge

class JudgeView(viewsets.ModelViewSet):
    serializer_class = JudgeSerializer
    queryset = Judge.objects.all()



