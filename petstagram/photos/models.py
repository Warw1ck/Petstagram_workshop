from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.pets.models import Pet
from petstagram.validators import size_validator


class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=(size_validator,))
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=False)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)