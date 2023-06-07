from django.urls import path

from petstagram.pets.views import pet_detail, add_pet, edit_pet, delete_pet

urlpatterns = [path('details/<username>/<slug>', pet_detail, name='pet-details'),
               path('pet-add', add_pet, name='pet-add'),
               path('pet-edit<username>/<pet_slug>', edit_pet, name='pet-edit'),
               path('pet-delete<username>/<pet_slug>', delete_pet, name='pet-delete'),]