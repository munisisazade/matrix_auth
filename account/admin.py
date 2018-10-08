import csv

from django.contrib import admin
from django.http import HttpResponse

from account.models import Workers, Picture, Article

def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format('contact_us_excell')
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response
# Register your models here.

export_as_csv.short_description = "Export to excell"

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('first_name', 'last_name', 'slug', 'email', 'description')
    actions = [export_as_csv,]


class PictureTabularInline(admin.TabularInline):
    model = Picture
    extra = 100




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PictureTabularInline, ]


