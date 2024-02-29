from django.contrib import admin
from .models import Project,ProjectTeam,Project_module,Task

# Register your models here.
admin.site.register(Project)
# admin.site.register(ProjectTeam)
# admin.site.register(Status)

@admin.register(ProjectTeam)
class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = ["user","project","status"]

@admin.register(Project_module)
class ProjectModuleName(admin.ModelAdmin):
    list_display = ["project","moduleName","description"]

@admin.register(Task)
class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ["Project","Module","title","priority","description","totalMinutes"]

