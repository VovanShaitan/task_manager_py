from django.db import models
from django_fsm import FSMField, transition
from main.models.user import User
from main.models.tag import Tag

class Task(models.Model):
    """Model definition for Task."""

    class Priority(models.TextChoices):
        IMMEDIATELY = "immediately"
        BY_MORNING = "by_morning"
        ON_MONDAY = "on_Monday"

    STATES = (
    "new_task",
    "in_development",
    "in_qa",
    "in_code_review",
    "ready_for_release",
    "released",
    "archived",
    )

    STATES = list(zip(map(str.upper, STATES), STATES))

    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateField()
    state = FSMField(default=STATES[0], choices=STATES)
    priority = models.CharField(
        max_length=255, default=Priority.IMMEDIATELY, choices=Priority.choices
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="author")
    assignee = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="assignee", default=None
    )
    tag = models.ManyToManyField(Tag)

    class Meta:
        """Meta definition for Task."""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    @transition(
        field=state,
        source=["new_task", "in_qa", "in_code_review"],
        target="in_development",
    )
    def to_state_to_in_development(self):
        pass

    @transition(field=state, source="in_development", target="in_qa")
    def to_state_to_in_qa(self):
        pass

    @transition(field=state, source="in_qa", target="in_code_review")
    def to_state_to_in_code_review(self):
        pass

    @transition(field=state, source="in_code_review", target="ready_for_release")
    def to_state_to_ready_for_release(self):
        pass

    @transition(field=state, source="ready_for_release", target="released")
    def to_state_to_released(self):
        pass

    @transition(field=state, source=["new_task", "released"], target="archived")
    def to_state_to_archived(self):
        pass

    def __str__(self):
        """Unicode representation of Task."""
        return self.title
