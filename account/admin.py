from django.contrib import admin
from account.models import Workers


# Register your models here.

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'description')
