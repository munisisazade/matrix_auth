from django.contrib import admin
from account.models import Workers


# Register your models here.

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('first_name', 'last_name', 'slug', 'email', 'description')
