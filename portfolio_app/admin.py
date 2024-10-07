from django.contrib import admin

# Register your models here.

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'technologies')
    search_fields = ('title', 'category', 'technologies')
    list_filter = ('category', 'date')