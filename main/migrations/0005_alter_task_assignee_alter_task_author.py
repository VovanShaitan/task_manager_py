# Generated by Django 4.1.3 on 2022-11-29 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_task_expired_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="task_assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="task_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]