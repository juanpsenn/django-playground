# Generated by Django 4.1.3 on 2022-12-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_active",
            field=models.BooleanField(default=True),
        )
    ]
