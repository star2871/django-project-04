from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "create_at", "updated_at")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("review", "user", "content")


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
