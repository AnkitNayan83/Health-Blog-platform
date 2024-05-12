from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.ArticlesLictCreate.as_view(), name="article-view-create"),

    path('articles/delete/<int:pk>/', views.ArticleDelete.as_view(), name="article-delete"),

    path('articles/<int:pk>/', views.ArticleViewUpdate.as_view(), name="article-view-update"),

    path("articles/<int:article_id>/comments/", views.CommentCreate.as_view(), name="comment-create"),
]