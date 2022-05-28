from .models import Comment, Post
from django import forms
from django.utils.html import strip_tags


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        content = strip_tags('content')
        fields = ('title', content,)
