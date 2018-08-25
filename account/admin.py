from django.contrib import admin
from account.models import Workers, Picture, Article


# Register your models here.

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('first_name', 'last_name', 'slug', 'email', 'description')


class PictureTabularInline(admin.TabularInline):
    model = Picture
    extra = 100


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PictureTabularInline, ]
