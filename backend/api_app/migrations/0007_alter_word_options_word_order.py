# Generated by Django 5.2 on 2025-05-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0006_alter_word_options_remove_word_order_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="word",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="word",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
