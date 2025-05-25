from rest_framework import serializers
from api_app.models import Sentence, Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ["id", "word_text", "order", "giphyURL"]


class SentenceSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, required=False)
    frontend_lookup_id = serializers.IntegerField(
        required=False, write_only=True, allow_null=True
    )

    class Meta:
        model = Sentence
        fields = ["id", "text", "words", "frontend_lookup_id"]

    def _handle_words(self, sentence_instance, words_data_list, is_update=False):
        if is_update:
            if words_data_list:
                words_to_crate = []
                words_to_delete = []
                existing_words = sentence_instance.words.all()
                # for word in words_data_list:
                #     if 

    # upsert logic:
    def _handle_words(self, sentence_instance, words_data_list, is_update=False):
        if is_update:
            sentence_instance.words.all().delete()

        if words_data_list:
            words_to_create = []
            for word_data in words_data_list:
                words_to_create.append(
                    Word(
                        sentence=sentence_instance,
                        word_text=word_data.get("word_text", ""),
                        order=word_data.get("order"),
                        giphyURL=word_data.get("giphyURL"),
                    )
                )
            if words_to_create:
                Word.objects.bulk_create(words_to_create)

    def create(self, validated_data):
        lookup_id = validated_data.pop("frontend_lookup_id", None)
        words_data = validated_data.pop("words", [])
        if lookup_id is not None:
            try:
                sentence_instance = Sentence.objects.get(id=lookup_id)
                for attr, value in validated_data.items():
                    setattr(sentence_instance, attr, value)
                sentence_instance.save()
                self._handle_words(sentence_instance, words_data, is_update=True)
                return sentence_instance

            except Sentence.DoesNotExist:
                new_sentence = Sentence.objects.create(**validated_data)
                self._handle_words(new_sentence, words_data, is_update=False)
                return new_sentence
        else:
            new_sentence = Sentence.objects.create(**validated_data)
            self._handle_words(new_sentence, words_data, is_update=False)
            return new_sentence

    def update(self, instance, validated_data):
        words_data = validated_data.pop("words")
        # frontend_lookup_id should never exist here
        validated_data.pop("frontend_lookup_id", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if words_data is not None:
            self._handle_words(instance, words_data, is_update=True)

        return instance
