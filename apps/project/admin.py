from django.contrib import admin
from apps.project.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ["name"]


admin.site.register(Project, ProjectAdmin)