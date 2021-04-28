from django.db import models

from joorab.apps.core.models import (
    SeoTagsBase,
    CreationModificationDateBase,
)

from joorab.apps.core.utils import upload_to


class MainCategory(SeoTagsBase, CreationModificationDateBase, models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(
        upload_to=upload_to(obj_type="categories/main/"),
        blank=True,
        null=True,
    )
    seo_post = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Category(SeoTagsBase, CreationModificationDateBase, models.Model):
    parent = models.ForeignKey("MainCategory", on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to=upload_to(obj_type="categories/subs/"),
        blank=True,
        null=True,
    )
    seo_post = models.TextField(blank=True)
    is_ghost = models.BooleanField(default=False)
    upper_content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.parent.title}: {self.tilte}"
