from typing import Any
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DeleteView,DetailView,UpdateView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam,Project_module,Task,UserTask
from .forms import ProjectTeamCreationForm,ProjectModuleForm,ProjectTaskForm,UserTaskForm
from user.models import User
from django.views import View
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
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Assigning the logged-in user to the 'user' field
        return super().form_valid(form)



class ProjectTeamList(ListView):
    # class ProjectStatusView(ListView):
    #     template_name = 'project/status.html'
    #     model = Status
    #     context_object_name = 'status'
    #     print(Status.objects.all())
    template_name = 'project/TableProjectTeam.html'
    context_object_name = "projectTeam"
    model = ProjectTeam
     
class ProjectTeamUpdate(CreateView):
    template_name = 'project/update_team.html'
    model = ProjectTeam
    form_class =   ProjectTeamCreationForm
    success_url = '/project/list/'

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        initial['project'] = project
        return initial
     
    



class ProjectDeleteView(DeleteView):
    template_name = 'project/delete_project.html'
    model = Project
    success_url = '/project/list/'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    template_name = 'project/detail_project.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_teams = ProjectTeam.objects.filter(project=self.object)
        # project_task = Task.objects.filter(Project=self.object)
        # project_module = Project_module.objects.filter(project=self.object)
        context['project_teams'] = project_teams  # Add ProjectTeam data to the context
        # context['project_task'] = project_task
        # context['project_module'] = project_module
        print("project : ",context['project_teams'])
        # print("task : ",context['project_task'])
        # print("module : ",context['project_module'])
        return context
    
    # def post(self, request, *args, **kwargs):
    #         # Handle form submission to add users to the project team
    #     project = self.get_object()
    #     user_id = request.POST.get('user_id')

    #     if user_id:
    #         user = User.objects.get(pk=user_id)
    #         # Check if the user is not already in the project team
    #         if not ProjectTeam.objects.filter(project=project, user=user).exists():
    #             project_team_member = ProjectTeam.objects.create(project=project, user=user)
    #             # Add any additional logic or messages as needed

    #     return self.get(request, *args, **kwargs)
    
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

    queryset = Task.objects.order_by('-title')
    #[mumbai,tokio]
    #[100000,200000]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
        
    return render(request, 'project/pie_chart.html',{
        'labels':labels,
        'data':data
    })        

# Project Report
    
class ProjectReport(DetailView):
    template_name = 'project/ProjectReport.html'
    model = Project
    context_object_name = 'projects'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_teams = ProjectTeam.objects.filter(project=self.object)
        project_teams_count = ProjectTeam.objects.filter(project=self.object).count()
        project_task = Task.objects.filter(Project=self.object)
        project_task_count = Task.objects.filter(Project=self.object).count()
        project_module = Project_module.objects.filter(project=self.object)
        project_module_count = Project_module.objects.filter(project=self.object).count()
        context['project_teams'] = project_teams  # Add ProjectTeam data to the context
        context['project_task'] = project_task
        context['project_module'] = project_module
        context['project_module_count'] = project_module_count
        context['project_task_count'] = project_task_count
        context['project_teams_count'] = project_teams_count
        print("project : ",context['project_teams'])
        print("task : ",context['project_task'])
        print("module : ",context['project_module'])
        return context
    
    
    
    