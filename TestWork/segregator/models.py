from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class RelationType(models.Model):
    class Meta:
        verbose_name = "Тип связи"
        verbose_name_plural = "Типы связей"

    type_name = models.CharField(max_length=255, verbose_name="Тип связи")

    def __str__(self):
        return self.type_name


class Relations(models.Model):
    class Meta:
        verbose_name = "Связь"
        verbose_name_plural = "Связи"

    rel_from = models.ForeignKey("Entity", on_delete=models.CASCADE, related_name="rel_from", verbose_name="Связь от")
    rel_type = models.ForeignKey("RelationType", on_delete=models.CASCADE, related_name="rel_types",
                                 verbose_name="Тип связи")
    rel_to = models.ForeignKey("Entity", on_delete=models.CASCADE, related_name="rel_to", verbose_name="Связь к")

    @property
    def get_short_from_title(self):
        __name__ = "Связь от"
        return f"{self.rel_from.title[:50]}..."

    def __str__(self):
        return f"{self.rel_from.slug} --({self.rel_type.type_name})-> {self.rel_to.slug}"


class Entity(MPTTModel):
    title = models.TextField(unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская сущность')
    slug = models.SlugField(db_index=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Сущность'
        verbose_name_plural = 'Сущности'

    def get_absolute_url(self):
        return reverse('entity-by-parents', args=[str(self.slug)])

    def __str__(self):
        return self.title
