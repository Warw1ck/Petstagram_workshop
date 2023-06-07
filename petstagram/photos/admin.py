from django.contrib import admin

# Register your models here.
from petstagram.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_publication', 'tagget_pets_list']

    @staticmethod
    def tagget_pets_list(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()] if obj.tagged_pets.all() else ['No tagget pets'])




admin.site.register(Photo, PhotoAdmin)
