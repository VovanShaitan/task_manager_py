from rest_framework.serializers import ModelSerializer
from main.models import User, Tag, Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone')
        fields = ("id", "username", "last_name", "first_name", "role", "email")


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "author",
            "assignee",
            "priority",
            "expired_at",
            "state",
            "tag",
        )


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")