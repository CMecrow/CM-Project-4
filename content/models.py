from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Archived"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=300)
    status = models.IntegerField(choices=STATUS, default=1)
    votes = models.ManyToManyField(User, related_name='post_votes', blank=True)
    # vote_count = models.IntegerField(votes, default='0')

    # class Meta:
    #     ordering = ['vote_count']

    # def __str__(self):
    #     return self.content

    def number_of_votes(self):
        return self.votes.count()


class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    # def __str__(self):
    #     return f"Comment {self.body} by {self.author}"