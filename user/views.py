from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from .models import User
from .forms import  ManagerRegistrationForm,UpdateProfile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project,Task,Project_module,ProjectTeam
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    # form = ManagerRegistrationForm(request.POST)
    # user = request.user
    # if form.is_valid():
    #     username = form.cleaned_data['username']
    #     email = form.cleaned_data['email']
    #     userImage = form.cleaned_data['userImage']
    #     role = form.cleaned_data['role']
    #     password1 = form.cleaned_data['password1']
    #     password2 = form.cleaned_data['password2']
    #     reg = User(username=username,email=email,userImage=userImage,role=role,password1=password1,password2=password2)
    #     reg.save()
        
    return render(request,"user/home.html")

def about(request):
    return render(request, "user/about.html")

def services(request):
    return render(request,"user/services.html")
def technology(request):
    return render(request,'user/technology.html')
def support(request):
    return render(request,'user/support.html')
class Home(CreateView):
    template_name = "user/home.html"
    model = User
    fomr_class = ManagerRegistrationForm

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')

class ManagerRegisterView(CreateView):
    template_name = "user/manager_register.html"
    model = User
    form_class =  ManagerRegistrationForm
    success_url = '/user/login/'


    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        # userImage = form.cleaned_data.get('userImage')
        # print(userImage)
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
    form_class = UpdateProfile
    success_url = '/user/userlist/'

    # def get_object(self, queryset=None):
    #         return self.request.user  # This assumes that the logged-in user is updating their own profile
    

    def form_valid(self, form):
            print('form : ',form)
            print("error : ",form.errors)
            return super().form_valid(form)   
    
class DeleteUser(DeleteView):
    template_name = 'user/DeleteUser.html'
    model = User
    success_url = '/user/userlist/'
    context_object_name = 'users'


class UserProfile(DetailView):
    template_name = 'user/UserProfile.html'
    model = User
    context_object_name = "userinfo"

def sendMail(to):
    subject = 'Welcome to PMS24'
    message = 'Hope you are enjoying your Django Tutorials'
    #recepientList = ["samir.vithlani83955@gmail.com"]
    recepientList = [to]
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
            
@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class ManagerDashboardView(ListView):
    # model = Task
    # print("task : ",Task)
    # context_object_name = 'tasks'
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        # print("ManagerDashboardView")           
        projects = Project.objects.all() #select * from project
        task = Task.objects.all()
        projectteam = ProjectTeam.objects.all()
        startedTask = Task.objects.filter(status="Started").count()
        processingTask = Task.objects.filter(status="Processing").count()
        completeTask = Task.objects.filter(status="Complted").count()
        HighTask = Task.objects.filter(priority="High").count()
        MediumTask = Task.objects.filter(priority="Medium").count()
        LowTask = Task.objects.filter(priority="Low").count()
        totalProject = Project.objects.all().count()
        totalModule = Project_module.objects.all().count()
        totalTask = Task.objects.all().count()
        totalUser = User.objects.all().count()
        # developer = ProjectTeam.filter(request.user.role == "Developer" )
        print("Started Task : ",startedTask)
        print("Processing Task : ",processingTask)
        print("complete Task : ",completeTask)
        # print(".............................................",projects)
        return render(request, 'user/manager_dashboard.html',{"projectteam":projectteam,"projects":projects,"task":task,"complteTask":completeTask,"processingTask":processingTask,"startedTask":startedTask,'TotalProject':totalProject,'Project_module':totalModule,'totalTask':totalTask,'totalUser':totalUser,'HighTask':HighTask,'MediumTask':MediumTask,'LowTask':LowTask })
    
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
    

