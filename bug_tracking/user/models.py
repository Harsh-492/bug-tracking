from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ROLE_CHOICES = (
    ("Manager","Manager"),
    ("Tester","Tester"),
    ("Developer","Developer"),
    ("Admin","Admin"),
)
 

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    salary = models.FloatField(null=True,blank=True)
    role = models.CharField(choices=ROLE_CHOICES,max_length=100,null=True,blank=True)
    is_manager = models.BooleanField(default = False)
    is_developer = models.BooleanField(default=False)
    userImage = models.ImageField(upload_to='uploads/',null=True)
    
    class Meta:
        db_table = 'user'        