from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Archived"), (1, "Published"))

class Post(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=600)
    status = models.IntegerField(choices=STATUS, default=1)
    votes = models.ManyToManyField(User, related_name='post_votes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

    def number_of_votes(self):
        return self.votes.count()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_text')
    body = models.TextField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"