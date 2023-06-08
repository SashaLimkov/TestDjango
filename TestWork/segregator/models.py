from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Entity(MPTTModel):
    title = models.TextField( verbose_name='Название')
    body = models.TextField("Содержание", blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская сущность')
    slug = models.SlugField(null=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Сущность'
        verbose_name_plural = 'Сущности'

    def get_absolute_url(self):
        return reverse('entity-by-parents', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Doc(models.Model):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
    file = models.FileField("Файл", upload_to="file")
    description = models.TextField("Описание документа", null=True, blank=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="entities", verbose_name="Оглавления", blank=True, default=None)

    def __str__(self):
        return self.description
