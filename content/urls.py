from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new_post/', views.CreatePost.as_view(), name='new_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='post_votes'),
    path('edit/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(),
         name='delete_post'),
]
