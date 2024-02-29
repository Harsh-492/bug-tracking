from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DeleteView,DetailView,UpdateView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam,Project_module,Task,UserTask
from .forms import ProjectTeamCreationForm,ProjectModuleForm,ProjectTaskForm,UserTaskForm

# Create your views here.

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'
    
class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'
    # print(status)
    # def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         model2_data = Status.objects.all()
    #         context['model2_data'] = model2_data
    #         print(model2_data)
    #         return context


class ProjectTeamCreateView(CreateView):    
    template_name = 'project/create_team.html'
    model = ProjectTeam
    success_url = '/project/list/'
    form_class = ProjectTeamCreationForm
    context_object_name = 'projects'

    def get_object(self, queryset=None):
        # Override get_object method to retrieve a single user object based on the ID provided in the URL
        return self.get_queryset().get(id=self.kwargs['pk'])
    



class ProjectTeamList(ListView):

    pass
    # class ProjectStatusView(ListView):
    #     template_name = 'project/status.html'
    #     model = Status
    #     context_object_name = 'status'
    #     print(Status.objects.all())
     

class ProjectDeleteView(DeleteView):
    template_name = 'project/delete_project.html'
    model = Project
    success_url = '/project/list/'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    template_name = 'project/detail_project.html'
    model = Project
    context_object_name = 'projects'

class ProjectUpdateView(UpdateView):
    template_name = 'project/update_project.html'
    form_class = ProjectCreationForm
    model = Project
    success_url = '/project/list/'
    



# Project Module------------->
class ProjectModuleView(CreateView):
    template_name = 'project/projectmodule.html'
    form_class = ProjectModuleForm
    model = Project_module
    success_url = '/project/projectmodulelist/'
    

class ProjectModuleList(ListView):
    template_name = 'project/TableProjectModule.html'
    model = Project_module
    context_object_name = 'modules'

class ProjectModuleUpdate(UpdateView):
    template_name = 'project/update_module.html'
    form_class = ProjectModuleForm
    model = Project_module
    success_url = '/project/projectmodulelist/'

class ProjectModuleDelete(DeleteView):
    template_name = 'project/delete_module.html'
    model = Project_module
    context_object_name = 'module'
    success_url = '/project/projectmodulelist/'



#  Tasks----------------->
class ProjectTaskView(CreateView):
    template_name = 'project/projectTask.html'
    form_class = ProjectTaskForm
    model = Task
    success_url = '/project/projecttasklist/'

class ProjectTaskList(ListView):
    template_name = 'project/TableProjectTask.html'
    model = Task
    context_object_name = 'tasks'


class ProjectTaskUpdate(UpdateView):
    template_name = 'project/update_task.html'
    model = Task
    form_class = ProjectTaskForm
    success_url = '/project/projecttasklist/'

class ProjectTaskDelete(DeleteView):
    template_name = 'project/delete_task.html'
    model = Task
    context_object_name = 'task'
    success_url = '/project/projecttasklist/'


def pieChart(request):
    labels = []
    data = []
     
    queryset = Project.objects.order_by('')