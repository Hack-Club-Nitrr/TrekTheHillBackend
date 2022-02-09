from django.db import models

# Create your models here.

role = (
    ("speaker", "speaker"),
    ("mentor", "mentor"),
)

class Speaker(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    designation = models.CharField(max_length=1050)
    linkedin = models.CharField(max_length=1050,blank=True)
    github = models.CharField(max_length=1050,blank=True)
    image = models.ImageField(upload_to='images')
    role = models.CharField(
        max_length=200,
        choices=role,
        default='web'
    )

    # body = models.TextField()

    def _str_(self):
        return self.name
