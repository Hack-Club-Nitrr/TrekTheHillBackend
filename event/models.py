from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120,)
    description = models.CharField(max_length=1050)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images')

    # body = models.TextField()

    def _str_(self):
        return self.title
