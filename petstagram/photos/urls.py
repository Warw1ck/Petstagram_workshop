from django.urls import path

from petstagram.photos.views import pet_details, add_photo, edit_photo, delete_photo

urlpatterns = [path('details/<int:pk>', pet_details, name='photo-details'),
               path('add-photo', add_photo, name='add-photo'),
               path('edit-photo<int:pk>', edit_photo, name='edit-photo'),
               path('delete-photo<int:pk>', delete_photo, name='delete-photo'),]