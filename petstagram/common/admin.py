from django.contrib import admin

# Register your models here.
from petstagram.common.models import Comments


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comments, CommentsAdmin)