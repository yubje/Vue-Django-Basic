from rest_framework import serializers
from .models import Article
from accounts.serializers import UserSerializer

# 게시글 목록 
class ArticleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title']

# 게시글 상세정보(게시글 작성)
class ArticleSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ['id', 'user', 'created_at', 'updated_at']