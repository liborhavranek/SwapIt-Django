from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'position', 'is_visible', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_visible', 'is_active')
    search_fields = ('name',)
