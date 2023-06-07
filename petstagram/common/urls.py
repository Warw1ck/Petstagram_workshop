from django.urls import path
from petstagram.common import views

urlpatterns = [path('', views.show_home_page, name='home page'),
               path('like/<int:id>', views.like_functionality, name='like'),
               path('share/<int:photo_id>', views.copy_to_clipboard, name='share'),
               path('comment/<int:photo_id>', views.add_comment, name='comment')
]
