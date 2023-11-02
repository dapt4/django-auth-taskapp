from .models import User, Task
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='email'
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done', 'user']
