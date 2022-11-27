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
        "tag"
        )
    list_display_links = ("id", "title")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")



# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)


# task_manager_admin_site.register(User, UserAdmin)
