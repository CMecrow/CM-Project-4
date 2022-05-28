from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.utils.text import slugify
from django.db.models import Count
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, CreateForm


# class PostList(generic.ListView):
#     model = Post
#     # queryset = Post.objects.filter(status=1).order_by(number_of_votes())
#     queryset = Post.objects.annotate(vote_count=Count('votes')).order_by('-vote_count')
#     queryset_by_date = Post.objects.order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 8

    # def get_success_url(self):
    #     return reverse('home', kwargs={'post_list': queryset, 'post_list_date': queryset_by_date})

class PostList(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'post_list_votes'
    model = Post
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context.update({
            'post_list_date': Post.objects.order_by('-created_on')[:8],
        })
        return context

    def get_queryset(self):
        return Post.objects.annotate(vote_count=Count('votes'))\
            .order_by('-vote_count')


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
                "voted": voted,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.order_by('created_on')
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment successfully submitted!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "voted": voted,
                "comment_form": comment_form,
            },
        )


class CreatePost(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "new_post.html",
            {
                "create_form": CreateForm()
            },
        )

    def post(self, request, *args, **kwargs):

        create_form = CreateForm(data=request.POST) 

        if create_form.is_valid():
            slug = slugify(create_form.instance.title)
            create_form.instance.slug = slug
            create_form.instance.author = request.user
            created_post = create_form.save(commit=False)
            created_post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post succesfully submitted!')
        else:
            create_form = CreateForm()

        return redirect('home',)


class PostVote(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.votes.filter(id=request.user.id).exists():
            post.votes.remove(request.user)
        else:
            post.votes.add(request.user)

        return redirect(reverse('post_detail', args=[slug]))


class EditPost(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = CreateForm(instance=post)

        return render(
            request,
            "edit_post.html",
            {
                "create_form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = CreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post successfuly edited!')
            return redirect(reverse('post_detail', args=[slug]))


class DeletePost(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = CreateForm(instance=post)
        return render(
            request,
            "delete_post.html",
            {
                "create_form": form,
                "post": post
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Post successfully deleted!')
        return redirect('home',)