# Generated by Django 4.0.1 on 2022-02-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='preference',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
