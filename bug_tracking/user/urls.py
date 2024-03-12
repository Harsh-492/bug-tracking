from django.contrib import admin
from django.urls import path
from .views import ManagerRegisterView,UserLoginView,ManagerDashboardView,DeveloperDashboardView,UserList,UpdateUser,UpdateTaskStatus
from django.contrib.auth.views import LogoutView,LoginView 


urlpatterns = [
    
    path('manager-register/',ManagerRegisterView.as_view(),name="manager-register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("dashboard/",ManagerDashboardView.as_view(),name="dashboard"),
    path("developer-dashboard/",DeveloperDashboardView.as_view(),name="developer-dashboard"),
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),

    path('status_update/<int:pk>/',UpdateTaskStatus.as_view(),name='status_update'),

    path('userlist/',UserList.as_view(),name='userlist'),
    path('userlist/<int:pk>',UserList.as_view(),name='userlist'),

    path('userupdate/<int:pk>',UpdateUser.as_view(),name='userupdate')

] 
