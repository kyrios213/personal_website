from django.contrib import admin

from .models import Profile, Projects


class ProjectsAdmin(admin.ModelAdmin):
    model = Projects
    list_display = [
        'name', 'created'
    ]


admin.site.register(Profile)
admin.site.register(Projects, ProjectsAdmin)