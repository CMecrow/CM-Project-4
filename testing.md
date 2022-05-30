# Testing

Testing on this project has been done both manually and through validators and linters. Detailed below are some of the test conducted, issues found and workarounds implimented.

## index.html / Post model / PostList view

- The first steps taken in the project, once the workspace had been set up with libraries installed, was to create the Post model. This model would be responsible for the main content of the site, the posts themselves. The base for the model was taken from the Code Institute 'I Think Therefore I Blog' walkthrough project and then tweaked to suit. For example the max length of title, slug and content were reduced. One of the main changes and challenges was adjusting the way posts were ordered on the page. Originally posts were aranged via date posted but for a site where users could post themselves, this didn't make as much sense. I attempted for a while to create a new variable in the Post model that would turn the ManytoMany vote field into an IntergerField so there could simply be a Meta class which would order by this new IntergerField but this wasn't successful. The solution was to employ [aggregation](https://docs.djangoproject.com/en/4.0/topics/db/aggregation/) in the PostList view, namely using .annotate and Count to tally up the vote field and store that in a new variable which could then be used to order the posts.
- As mentioned this view had been created in the same structure as the walkthrough project, where a generic.ListView suited perfectly as it would do the work for us and would contain the variables required already such as paginate_by. However this became a problem when I tried to have a second ordering system for the second set of posts on the homepage. The difficulty here was that the solution I found [here](https://stackoverflow.com/questions/31133963/multiple-models-generic-listview-to-template), involved editing some of the existing variables within generic.ListView namely 'context_object_name' and 'context'. This could have been avoided by not using a ListView to begin with, but as the issue was found well into the project, I decided to employ this slight brute foce method, rather than rebuilding the view entirely. Were the project to be revisited and refined, this is something I'd prioritise changing. 
- Although I mentioned this in the readme, it's worth discussing here, there are fields in the Post and Comment model that are being stored but not used in the current iteration of the project, the 'updated_on' DateTime fields. I was concerned that the pages were becoming very text heavy, especially when some of the opinions posted were once sentence, already having the author, created on date, time and the vote and comment counters, there was a risk that the information about the post would outweigh the post itself. I kept both of these fields within their respective models because it's information that may be useful to use or display to the user in future iterations of the project. As it stands posts could be edited after posting to make the comments look strange and out of place, it wouldn't be clear to a site user why this was the case. If the updated on information was displayed to the user to show that this post had been edited after posting, this may fix this potential problem.

## post_detail.html / Comment model / PostDetail view

- The main issue that I encountered with the Comment model was having the comment author field a ForeignKey taken from User in the comment model. When trying to submit a comment the user would get the error 'null value in column "author_id"'. The workaround for this was to instead set the author from the PostDetail view with the code:

            comment_form.instance.author = request.user.username

    Because the comment author was no longer being set from within the model, it could be changed from a ForeignKey to a CharField, solving the error.

## edit_post.html / EditPost view

- An unexpected issue with the edit post functionality occured when retreiving the completed form with:

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

    Within edit_post.html, the populated form data would contain html tags. Many different fixes were attempted through django, using methods like 'safe' and 'strip_tags' without success. It was then noticed that this wasn't an error that was occuring on every post. I realised that the only posts that were being retrieved displaying html tags were the posts created with Summernote in the admin page. When I first made the project I populated it with posts created from the admin panel, a feature that has fallen to be obsolete with the ease of adding posts from the main new post page. There was not a fix found to remove the html tags from Summernote posts when they were retrieved via the EditPost view, so this is an area that would require some investigation. I don't believe this hinders the project as should the admin wish to post to the site, the general user accessible post pages are actually much more convenient and simpler to use.

## urls.py

- One error on my part that caused confusion was the ordering of the url paths in urls.py. When attempting to set up the CreatePost view and template, I would receive a 404 error referencing the PostDetail view. The problem turned out to be that the PostDetail view took the user to the following url path:

            path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    As this path contained 'slug:slug', the new_post url was read as a slug, so django was trying to find a post with that slug, hence the 404.
    The solution was actually very simple, because django reads available urls from top to bottom, the CreatePost url path:

            path('new_post/', views.CreatePost.as_view(), name='new_post'),
    Simply had to be placed above the PostDetail url path.

## Linting issues

- There are linting issues in views.py as the linter is looking for 'Post' for example in that file, when it is actually being imported from models.py. Because the linter can not find Post, it cannot find any objects relating to it so it is giving an incorrect error of 'Class Post has no objects member'.
    

