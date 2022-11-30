from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task, Tag


class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "author",
        "assignee",
        "priority",
        "expired_at",
        "state",
    )
    list_editable = (
        "expired_at",
        "state",
        "priority",
        "assignee",
    )
    ordering = ("expired_at",)


class CustomAdmin(UserAdmin):
    model = User
    list_display = ("username", "last_name", "first_name", "role", "email")
    list_editable = ("role",)


task_manager_admin_site.register(User, CustomAdmin)
