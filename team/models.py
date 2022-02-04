from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=120,)
    email = models.EmailField(max_length=120)
    designation = models.CharField(max_length=1050)
    phone = models.CharField(max_length=10,blank=True)
    instagram = models.CharField(max_length=1050,blank=True)
    facebook = models.CharField(max_length=1050,blank=True)
    linkedin = models.CharField(max_length=1050,blank=True)
    twitter = models.CharField(max_length=1050,blank=True)

    image = models.ImageField(upload_to='images')

    # body = models.TextField()

    def _str_(self):
        return self.name
