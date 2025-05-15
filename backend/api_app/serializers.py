from rest_framework import serializers
from api_app.models import Sentence, Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ["id", "word_text", "order", "giphyURL"]


class SentenceSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, required=False)

    class Meta:
        model = Sentence
        fields = ["id", "words", "text"]

    def create(self, validated_data):
        sentence = Sentence.objects.create(**validated_data)
        words_list = validated_data.get("text").split()
        # TODO: add logic for retrieving giphyURLS for the word_list and adding it to each word
        for order_index, word_text in enumerate(words_list):
            Word.objects.create(
                sentence=sentence, order=order_index, word_text=word_text
            )
        return sentence

    def update(self, instance, validated_data):
        existing_words_list = instance.words.all()
        new_words_list = validated_data.get("text").split()
