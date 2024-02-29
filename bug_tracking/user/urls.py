from django.contrib import admin
from django.urls import path
from .views import ManagerRegisterView,UserLoginView,ManagerDashboardView,DeveloperDashboardView,UserList,UpdateUser
from django.contrib.auth.views import LogoutView,LoginView 


urlpatterns = [
    
    path('manager-register/',ManagerRegisterView.as_view(),name="manager-register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("manager-dashboard/",ManagerDashboardView.as_view(),name="manager-dashboard"),
    path("developer-dashboard/",DeveloperDashboardView.as_view(),name="developer-dashboard"),
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),

    path('userlist/',UserList.as_view(),name='userlist'),
    path('userlist/<int:pk>',UserList.as_view(),name='userlist'),

    path('userupdate/<int:pk>',UpdateUser.as_view(),name='userupdate')

] 
