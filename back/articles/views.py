from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def index(request):
  articles = Article.objects.order_by('-pk')
  serializer = ArticleListSerializer(articles, many=True)
  return Response(serializer.data)
