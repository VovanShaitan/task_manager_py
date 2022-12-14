from main.models.tag import Tag
from main.models.task import Task
from main.models.user import User
from main.serializers import TagSerializer, TaskSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer


class TaskViewSet(ModelViewSet):
    queryset = (
        Task.objects.select_related("author", "assignee")
        .prefetch_related("tag")
        .order_by("id")
    )
    serializer_class = TaskSerializer
