from django import forms
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only the contents of the comment will be inserted

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only allow insertion of comment content