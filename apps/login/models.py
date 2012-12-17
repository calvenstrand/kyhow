from django.contrib.auth.models import *
from django.db import models
from django.forms import ModelForm

class UserLogin(models.Model):
    user = models.OneToOneField(User)
    
    
class UserLoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        