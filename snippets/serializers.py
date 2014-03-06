from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):

	class Meta:
		model=Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

	def restore_object(self, attrs, instance=None):
		"""
		Create or update a new snippet instance, given a dictionary
		of deserialized field values.

		Note that if we don't define this method, then deserializing
		data will simply return a dictionary of items.
		"""
                      owner = serializers.Field(source='owner.username')
		if instance:
			instance.title = attrs.get('title', instance.title)
			instance.code = attrs.get('code', instance.code)
			instance.linenos = attrs.get('linenos', instance.linenos)
			instance.language = attrs.get('language', instance.language)
			instance.style = attrs.get('style', instance.style)
			return instance
		return Snippet(**attrs)

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ('id,'' 'username', 'snippets)'