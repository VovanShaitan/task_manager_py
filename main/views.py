from main.models.tag import Tag
from main.models.task import Task
from main.models.user import User
from main.permissions import OnlyStaffCanDeletedObjectPermission
from main.serializers import TagSerializer, TaskSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("first_name",)


class TaskFilter(django_filters.FilterSet):
    author = django_filters.ModelChoiceFilter(
        lookup_expr="icontains", queryset=User.objects.all()
    )
    assignee = django_filters.ModelChoiceFilter(
        lookup_expr="icontains", queryset=User.objects.all()
    )
    state = django_filters.ChoiceFilter(choices=Task.STATES)
    tag = django_filters.ModelMultipleChoiceFilter(
        field_name="tag__title",
        lookup_expr="icontains",
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Task
        fields = ("author", "assignee", "state", "tag")


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
    permission_classes = [OnlyStaffCanDeletedObjectPermission]


class TaskViewSet(ModelViewSet):
    queryset = (
        Task.objects.select_related("author", "assignee")
        .prefetch_related("tag")
        .order_by("id")
    )
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    permission_classes = [OnlyStaffCanDeletedObjectPermission]
