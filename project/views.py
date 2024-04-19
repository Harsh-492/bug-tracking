from typing import Any
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DeleteView,DetailView,UpdateView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam,Project_module,Task
from .forms import ProjectTeamCreationForm,ProjectModuleForm,ProjectTaskForm,UserTaskForm
from django.core.mail import send_mail
from django.conf import settings
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
    
class ProjectUpdateView(UpdateView):
    template_name = 'project/update_project.html'
    form_class = ProjectCreationForm
    model = Project
    success_url = '/project/list/'
    


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
    

    def form_valid(self, form):
        
        user = form.cleaned_data.get('user')
        email = user.email
        userName = user.first_name
        project_id = self.kwargs.get('project_id')
        # userImage = form.cleaned_data.get('userImage')
        # print(userImage)
        print("email....",email)
        print("projectID....",project_id)
        print("userName....",userName)
        if sendMail(email,project_id,userName):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
     
    


def sendMail(to,project_id,userName):
    project = Project.objects.get(id=project_id)
    subject = 'Task Assignment'
    # message = 'Hope you are enjoying your Django Tutorials' + 'project is ' + project.name
    message = '''
Dear ''' +  userName + ''',

I hope this message finds you well. I'm writing to assign you a task that aligns with your expertise and responsibilities within the team. Below are the details of the task:

Project : ''' + project.name + '''
Description:  ''' + project.description + '''
Technology: ''' + project.technology + '''
Instructions: Complete The Project as soon as Possible And Then  Submit the Result to us.

Please review the task details carefully and let me know if you have any questions or need further clarification. Your prompt attention to this matter is greatly appreciated.

Thank you for your continued dedication and contribution to our team's success.

Best regards,
Manager
98989 67543
'''

    #recepientList = ["samir.vithlani83955@gmail.com"]
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    #attach file
    #html
    return True

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
        total_hours_spent = (task.total_hours_spent() for task in project_task)
        context['total_hours_spent'] = total_hours_spent
        print("project : ",context['project_teams'])
        print("task : ",context['project_task'])
        print("module : ",context['project_module'])
        print("total_hours_spent : ",context['total_hours_spent']) 
        return context