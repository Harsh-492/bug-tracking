from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from .models import User
from .forms import  ManagerRegistrationForm,DeveloperRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project,Task,Project_module

# Create your views here.
def index(request):
    return render(request,"index.html")

class ManagerRegisterView(CreateView):
    template_name = "user/manager_register.html"
    model = User
    form_class =  ManagerRegistrationForm
    success_url = '/user/login/'

       
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        userImage = form.cleaned_data.get('userImage')
        print(userImage)
        print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
        
class UserList(ListView):
    template_name = 'user/Tableuser.html'
    model = User
    context_object_name = 'users'

class UpdateUser(UpdateView):
    template_name = 'user/UpdateUser.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/user/userlist/'
    
    # def form_valid(self, form):
    #         print('form : ',form)
    #         print("error : ",form.errors)
    #         return super().form_valid(form)   
    
    # def form_valid(self, form):
    #     form.instance.user = self.request.user  # Assigning the logged-in user to the 'user' field
    #     print("form : ",form)
    #     return super().form_valid(form)
    
class DeleteUser(DeleteView):
    template_name = 'user/DeleteUser.html'
    model = User
    success_url = '/user/userlist/'
    context_object_name = 'users'


class UserProfile(DetailView):
    template_name = 'user/UserProfile.html'
    model = User
    context_object_name = "userinfo"


class DeveloperRegisterView(CreateView):
    template_name = "user/developer_register.html"
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/login/'


def sendMail(to):
    subject = 'Welcome to PMS24'
    message = 'Hope you are enjoying your Django Tutorials'
    #recepientList = ["samir.vithlani83955@gmail.com"]
    recepientList = ['to']
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    #attach file
    #html
    return True


class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/dashboard/'
            else:
                return '/user/dashboard/'
            

class ManagerDashboardView(ListView):
    # model = Task
    # print("task : ",Task)
    # context_object_name = 'tasks'
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        # print("ManagerDashboardView")           
        projects = Project.objects.all() #select * from project
        task = Task.objects.all()
        
        startedTask = Task.objects.filter(status="Started").count()
        processingTask = Task.objects.filter(status="Processing").count()
        completeTask = Task.objects.filter(status="Complted").count()
        totalProject = Project.objects.all().count()
        totalModule = Project_module.objects.all().count()
        totalTask = Task.objects.all().count()
        totalUser = User.objects.all().count()
        print("Started Task : ",startedTask)
        print("Processing Task : ",processingTask)
        print("complete Task : ",completeTask)
        # print(".............................................",projects)
        
        return render(request, 'user/manager_dashboard.html',{"projects":projects,"task":task,"complteTask":completeTask,"processingTask":processingTask,"startedTask":startedTask,'TotalProject':totalProject,'Project_module':totalModule,'totalTask':totalTask,'totalUser':totalUser})
    
    template_name = 'user/manager_dashboard.html'


class UpdateTaskStatus(View):
    def post(self,request,pk):
        task = Task.objects.get(id=pk)

        if task.status == "Started":
            task.status = "Processing"
        elif task.status == "Processing":
            task.status = "Complted"
        else:
            task.status = "Started"

        task.save()

        return redirect(reverse('dashboard'))
    

class DeveloperDashboardView(ListView):
    template_name = 'user/developer_dashboard.html' 
    model = Project
    context_object_name = 'projects'
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/developer_dashboard.html')
    

