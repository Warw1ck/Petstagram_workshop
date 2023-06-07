from django.db import models

# Create your models here.
from petstagram.photos.models import Photo


class Comments(models.Model):
    text = models.TextField(max_length=300)
    date_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

