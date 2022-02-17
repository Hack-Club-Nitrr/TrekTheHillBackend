from django.db import models
SPONSER_CATEGORY = (
    ('diamond','DIAMOND'),
    ('platinum', 'PLATINUM'),
    ('gold','GOLD'),
    ('silver','SILVER'),
    ('bronze','BRONZE'),
    ('community_partner','COMMUNITY PARTNER')
)

class Sponser(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    category= models.CharField(max_length=20, choices=SPONSER_CATEGORY, default='diamond')

    def _str_(self):
        return self.name