from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task, Tag

# class TaskManagerAdminSite(admin.AdminSite):
#     pass

# task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")

# @admin.register(Tag, site=task_manager_admin_site)
# class TagAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Task, site=task_manager_admin_site)
# class TaskAdmin(admin.ModelAdmin):
#     pass


class CustomAdmin(UserAdmin):
    list_display = ("username", "last_name", "first_name", "role", "email")
    list_display_links = ("username",)



class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "created_at",
        "updated_at",
        "expired_at",
        "state",
        "priority",
        "assignee",
        "author",
        # "tags"
        )
    list_display_links = ("id", "title")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")



admin.site.register(User, CustomAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)


# task_manager_admin_site.register(User, UserAdmin)
