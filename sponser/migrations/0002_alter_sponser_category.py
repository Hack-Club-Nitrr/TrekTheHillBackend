# Generated by Django 4.0.1 on 2022-02-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponser',
            name='category',
            field=models.CharField(choices=[('diamond', 'DIAMOND'), ('platinum', 'PLATINUM'), ('gold', 'GOLD'), ('silver', 'SILVER'), ('bronze', 'BRONZE'), ('community_partner', 'COMMUNITY PARTNER')], default='diamond', max_length=20),
        ),
    ]