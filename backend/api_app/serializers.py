from rest_framework import serializers
from api_app.models import Sentence


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ["text"]
