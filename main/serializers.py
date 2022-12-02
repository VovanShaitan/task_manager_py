from rest_framework.serializers import ModelSerializer
from main.models import user, tag, task


class UserSerializer(ModelSerializer):
    class Meta:
        model = user.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(ModelSerializer):
    class Meta:
        model = tag.Tag
        fields = ("id", "title")


class TaskSerializer(ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = task.Task
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
