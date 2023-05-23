from django.contrib import admin
from django.forms import TextInput, Textarea

# Register your models here.
from django.db import models
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Entity, Relations, RelationType
from import_export.admin import ExportActionMixin


class RelationsFromInline(admin.StackedInline):
    model = Relations
    fk_name = "rel_from"


class RelationsToInline(admin.StackedInline):
    model = Relations
    fk_name = "rel_to"


class RelationsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("get_short_from_title", "rel_type", "rel_to")
    readonly_fields = ("rel_from", "rel_type", "rel_to")
    list_display_links = ("get_short_from_title", "rel_to")


class EntityAdmin(ExportActionMixin, DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [RelationsFromInline, RelationsToInline]


admin.site.register(RelationType)
admin.site.register(Relations, RelationsAdmin)
admin.site.register(Entity, EntityAdmin)
