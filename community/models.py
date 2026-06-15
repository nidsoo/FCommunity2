from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='games/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    download_link = models.URLField()

    def __str__(self):
        return self.name