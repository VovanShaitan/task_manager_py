# Generated by Django 4.1.3 on 2022-11-28 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_tag_user_role_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="state",
            field=django_fsm.FSMField(
                choices=[
                    ("NEW_TASK", "new_task"),
                    ("IN_DEVELOPMENT", "in_development"),
                    ("IN_QA", "in_qa"),
                    ("IN_CODE_REVIEW", "in_code_review"),
                    ("READY_FOR_RELEASE", "ready_for_release"),
                    ("RELEASED", "released"),
                    ("ARCHIVED", "archived"),
                ],
                default=("NEW_TASK", "new_task"),
                max_length=50,
            ),
        ),
    ]