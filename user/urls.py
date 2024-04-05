from django.contrib import admin
from django.urls import path
from .views import about,services,technology,support,ManagerRegisterView,UserLoginView,ManagerDashboardView,DeveloperDashboardView,UserList,UpdateUser,UpdateTaskStatus,DeleteUser,UserProfile,Home
from django.contrib.auth.views import LogoutView,LoginView 


urlpatterns = [
    

    path('',Home.as_view(),name='home'),
    path('about/',about,name='about'),
    path('services/',services,name='services'),
    path('technology/',technology,name='technology'),
    path('supprt/',support,name='support'),
    path('manager-register/',ManagerRegisterView.as_view(),name="manager-register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("dashboard/",ManagerDashboardView.as_view(),name="dashboard"),
    path("developer-dashboard/",DeveloperDashboardView.as_view(),name="developer-dashboard"),
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),

    path('status_update/<int:pk>/',UpdateTaskStatus.as_view(),name='status_update'),

    path('userlist/',UserList.as_view(),name='userlist'),
    path('userlist/<int:pk>',UserList.as_view(),name='userlisti'),

    path('userupdate/<int:pk>',UpdateUser.as_view(),name='userupdate'),
    path('userdelete/<int:pk>',DeleteUser.as_view(),name='userdelete'),
    path('userprofile/<int:pk>',UserProfile.as_view(),name='userprofile'),


] 
