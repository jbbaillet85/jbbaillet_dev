from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy


# Create your models here.
class Project(models.Model):
    name = models.CharField(
        max_length=255, unique=True,
        verbose_name="project", default=""
    )
    slug = AutoSlugField(gettext_lazy("Slug"), populate_from=("name",))

    class Meta:
        verbose_name = "project"

    def __str__(self):
        """
        The string representation of this model is the slug.
        """
        return self.slug