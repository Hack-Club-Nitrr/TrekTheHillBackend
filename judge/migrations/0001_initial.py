# Generated by Django 4.0.1 on 2022-03-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('designation', models.CharField(blank=True, max_length=1050)),
                ('linkedin', models.CharField(blank=True, max_length=1050)),
                ('github', models.CharField(blank=True, max_length=1050)),
                ('image', models.ImageField(upload_to='images')),
                ('preference', models.CharField(max_length=2)),
            ],
        ),
    ]