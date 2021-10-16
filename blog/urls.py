from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name ='post_edit'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(), name ='post_delete'),
    path('post/<pk>/publish', views.publish_post, name='publish_post'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve', views.approve_comment, name='approve_comment'),
    path('comment/<pk>/delete', views.delete_comment, name='delete_comment'),
]