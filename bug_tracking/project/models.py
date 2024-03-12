from django.db import models

# Create your models here.
from django.db import models
from user.models import User

# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    projectimg = models.ImageField(upload_to= 'project/',null=True,blank=True)
    
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.name    

status_choices = (
    ("Started","Started"),
    ("Complted","Complted"),
    ("Processing","Processing"),
)

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True)        
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return self.user.username    
    
    

class Project_module(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    moduleName = models.CharField(max_length = 100)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'project_module'

    def __str__(self):
        return self.moduleName

# class Status(models.Model):
#     project = models.ForeignKey(Project,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     statusName = models.CharField(choices=status_choices,max_length=100)


class Task(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Module = models.ForeignKey(Project_module,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    totalMinutes = models.IntegerField()
    status = models.CharField(choices=status_choices,max_length=100,null=True,blank=True)

    class Meta:
        db_table = "Task"
    

class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

   



