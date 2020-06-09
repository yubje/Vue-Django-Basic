from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET'])
def index(request):
  articles = Article.objects.order_by('-pk')
  serializer = ArticleListSerializer(articles, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create(request):
  serializer = ArticleSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  serializer = ArticleSerializer(article)
  return Response(serializer.data)
