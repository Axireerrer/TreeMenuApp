from django.contrib import admin
from .models import Menu, Items


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    list_display_links = ['title']


@admin.register(Items)
class AdminItems(admin.ModelAdmin):
    list_display = ['menu', 'title', 'parent']
    list_filter = ['menu', 'title']
    search_fields = ['menu', 'title']
    list_display_links = ['menu', 'title', 'parent']