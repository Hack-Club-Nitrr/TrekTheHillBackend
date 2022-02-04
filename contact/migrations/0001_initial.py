# Generated by Django 4.0.1 on 2022-02-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
