from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ManagerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'salary','role', 'userImage', 'password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userImage'].required = False

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save()
        return user

class UpdateProfile(forms.ModelForm):
       class Meta:
            model = User
            fields =['username','first_name','last_name', 'email', 'age', 'salary','role', 'userImage']
            required = {
                 'username':False
            }


        



