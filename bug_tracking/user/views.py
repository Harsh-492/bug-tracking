from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import User
from .forms import  ManagerRegistrationForm,DeveloperRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project
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
    template_name = 'user/Profile.html'
    form_class = ManagerRegistrationForm
    model = User
    success_url = '/user/manager-dashboard/'
    
        
# class UserRegisterView(CreateView):
#     template_name = "user/user_register.html"
#     model = User
#     form_class = 


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
                return '/user/manager-dashboard/'
            else:
                return '/user/developer-dashboard/'
            

class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        print("ManagerDashboardView")           
        projects = Project.objects.all() #select * from project
        print(".............................................",projects)
        
        return render(request, 'user/manager_dashboard.html',{"projects":projects})
    
    
    template_name = 'user/manager_dashboard.html'

class DeveloperDashboardView(ListView):
    template_name = 'user/developer_dashboard.html' 
    model = Project
    context_object_name = 'projects'
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/developer_dashboard.html')
    
