from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo,Feedback
from django.forms import ModelForm

class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())

     class Meta():
         model = User
         fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields =  '__all__'
