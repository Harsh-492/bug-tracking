from django.contrib import admin
from django.urls import path, include
from .views import ProjectCreationView,ProjectListView,ProjectTeamCreateView,ProjectDeleteView,ProjectDetailView,ProjectUpdateView,ProjectModuleView,ProjectTaskView,ProjectModuleList,ProjectModuleUpdate,ProjectModuleDelete,ProjectTaskList,ProjectTaskUpdate,ProjectTaskDelete

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("list/",ProjectListView.as_view(),name="project_list"),
#  path("status/",ProjectStatusView.as_view(),name="project_status"),
 path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
#  path("update_team/<int:pk>",ProjectTeamUpdate.as_view(),name="update_team"),

 path("project_delete/<int:pk>",ProjectDeleteView.as_view(),name="project_delete"),
 path("project_detail/<int:pk>",ProjectDetailView.as_view(),name="project_detail"),
 path("project_update/<int:pk>",ProjectUpdateView.as_view(),name="project_update"),

 path("projectmodule/",ProjectModuleView.as_view(),name="projectmodule"),
 path("projectmodulelist/",ProjectModuleList.as_view(),name="projectmodulelist"),
 path("projectmoduleupdate/<int:pk>",ProjectModuleUpdate.as_view(),name="projectmoduleupdate"),
 path("projectmoduledelete/<int:pk>",ProjectModuleDelete.as_view(),name="projectmoduledelete"),



 path('projecttask/',ProjectTaskView.as_view(),name='projecttask'),
 path('projecttaskupdate/<int:pk>',ProjectTaskUpdate.as_view(),name='projecttaskupdate'),
 path('projecttaskdelete/<int:pk>',ProjectTaskDelete.as_view(),name='projecttaskdelete'),
 path('projecttasklist/',ProjectTaskList.as_view(),name='projecttasklist'),



 
]