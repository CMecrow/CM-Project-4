from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.order_by('created_on')
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "voted": voted
            }
        )