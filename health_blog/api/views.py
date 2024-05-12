from rest_framework import generics
from .models import Articles, Comments
from .serializers import ArticleSerializer, UserSerializer
from .commentSerializer import CommentSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class ArticlesLictCreate(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q',None)
        if query:
            return Articles.objects.filter(title__icontains=query)
        return Articles.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class ArticleDelete(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Articles.objects.filter(author=user)
    
class ArticleViewUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Articles.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["populate_author"] = True
        return context
    def perform_update(self, serializer):
        article = self.get_object()
        if article.author != self.request.user:
            raise PermissionDenied("You are not allowed to update this article")
        serializer.save()

    def perform_create(self, serializer):
        article = Articles.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, article=article)
    
    def get_object(self):
        article = super().get_object()
        article.comments.all()
        return article

class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = self.request.user
            article = Articles.objects.get(pk=self.kwargs['article_id'])
            serializer.save(author=user, article=article)
        else:
            print(serializer.errors)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
