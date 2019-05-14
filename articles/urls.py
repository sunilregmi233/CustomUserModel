from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
    CommentDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('comment/', CommentCreateView.as_view(), name='comment_new'),
    path('article/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('', ArticleListView.as_view(), name='article_list'),
]