
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *




class User_Form(UserCreationForm):
    #img_profile=forms.ImageField(label='add_your_image',required=True)
    #is_staff=forms.BooleanField(widget=forms.CheckboxInput(),required=True)
    
    class Meta:
        model=User
        fields={'username','password1','password2'}


class Web_form(forms.ModelForm):
      logo=forms.ImageField(label="add your company logo")
      class Meta:
        model=WebSite_owner
        fields="__all__"