from rest_framework import generics, permissions  # type: ignore
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    