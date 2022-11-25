from django.db import models


class Tag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        """Unicode representation of Tag."""
        pass
