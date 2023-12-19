from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        'Название',
        max_length=255,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        order_insertion_by = ['name']
        level_attr = 'mptt_level'


class Product(models.Model):
    name = models.CharField(
        'Name',
        max_length=255,
    )
