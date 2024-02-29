from django import forms
from .models import Project,ProjectTeam,Project_module,Task,UserTask


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields ='__all__'        
        
class ProjectModuleForm(forms.ModelForm):
    class Meta:
        model = Project_module
        fields = '__all__'

class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = '__all__'

# class ProjectStatusForm(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields ='__all__' 
        