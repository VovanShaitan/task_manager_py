# Generated by Django 4.1.3 on 2022-11-29 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_task_assignee_alter_task_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="task_assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
