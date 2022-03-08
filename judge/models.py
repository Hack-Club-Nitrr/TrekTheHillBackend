from django.db import models

# Create your models here.



class Judge(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120,blank=True)
    designation = models.CharField(max_length=1050,blank=True)
    linkedin = models.CharField(max_length=1050,blank=True)
    github = models.CharField(max_length=1050,blank=True)
    image = models.ImageField(upload_to='images')
 
    preference= models.CharField(max_length=2)
    # body = models.TextField()

    def _str_(self):
        return self.name
