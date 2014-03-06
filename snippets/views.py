from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
												 IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
