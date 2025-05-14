from rest_framework import serializers
from api_app.models import Sentence, Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ["id", "word_text", "giphyURL"]


class SentenceSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, required=False)

    class Meta:
        model = Sentence
        fields = ["id", "words", "text"]

    def create(self, validated_data):
        sentence = Sentence.objects.create(**validated_data)
        words_list = validated_data.get("text", "").split()
        for word in words_list:
            Word.objects.create(sentence=sentence, word_text=word)
        return sentence

    def update(self, instance, validated_data):
        current_words_data = instance.pop("words", [])
        words_data = validated_data.pop("words", [])
