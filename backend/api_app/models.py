from django.db import models


# Create your models here.
class Sentence(models.Model):
    text = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Word(models.Model):
    sentence = models.ForeignKey(
        Sentence, on_delete=models.CASCADE, related_name="words"
    )
    word_text = models.CharField(max_length=100)
    giphyURL = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.word_text
