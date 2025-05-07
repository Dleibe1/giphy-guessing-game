from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Sentence
from api_app.serializers import SentenceSerializer


# Create your views here.
class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
