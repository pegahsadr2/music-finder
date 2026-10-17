from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True, blank=True)
    file_path = models.TextField(unique=True)
    def __str__(self):
        return self.title