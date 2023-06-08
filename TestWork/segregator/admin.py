from django.contrib import admin
from django.forms import TextInput, Textarea

# Register your models here.
from django.db import models
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Entity, Doc
from import_export.admin import ExportActionMixin


class DocumentsInline(admin.StackedInline):
    model = Doc
    extra = False
    # readonly_fields = ("description","file")
    show_change_link=True


# class RelationsToInline(admin.StackedInline):
#     model = Relations
#     fk_name = "rel_to"


# class RelationsAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ("get_short_from_title", "rel_type", "rel_to")
#     readonly_fields = ("rel_from", "rel_type", "rel_to")
#     list_display_links = ("get_short_from_title", "rel_to")

    

class EntityAdmin(ExportActionMixin, DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (DocumentsInline,)

# admin.site.register(RelationType)
# admin.site.register(Relations, RelationsAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Doc)