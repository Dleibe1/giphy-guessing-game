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
        fields = ["id", "text", "words"]

    def create(self, validated_data):
        words_data = validated_data.pop("words", [])
        try:
            new_sentence = Sentence.objects.create(**validated_data)
            self._handle_words(new_sentence, words_data)
            return new_sentence
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def update(self, instance, validated_data):
        words_data = validated_data.pop("words")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if words_data is not None:
            self._handle_words(instance, words_data)

        return instance

    def _handle_words(self, sentence_instance, words_data_list):
        if not words_data_list:
            sentence_instance.words.all().delete()
            return

        words_to_create = []
        for incoming_word_data in words_data_list:
            incoming_word_id = incoming_word_data.get("id")
            
            if incoming_word_id is not None:
                try:
                    word_instance = Word.objects.get(id=incoming_word_id)
                    word_instance_order = word_instance.order
                    incoming_word_order = incoming_word_data.get("order")
                    if word_instance_order is not incoming_word_order:
                        word_instance.order = incoming_word_order
                        word_instance.save()
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                words_to_create.append(
                    Word(
                        sentence=sentence_instance,
                        word_text=incoming_word_data.get("word_text"),
                        order=incoming_word_data.get("order"),
                        giphyURL=incoming_word_data.get("giphyURL"),
                    )
                )
                
        if words_to_create:
                Word.objects.bulk_create(words_to_create)