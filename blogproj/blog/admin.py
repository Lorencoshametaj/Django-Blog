from django.contrib import admin
from .models import Comment
# Register your models here.
from django.contrib import admin
from .models import Post

# Register the Post template to make it visible in the admin panel

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('author__username', 'body')

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(Comment, CommentAdmin)