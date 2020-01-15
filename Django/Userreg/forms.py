from django import forms
from Userreg.models import UserProfileInfo
from django.contrib.auth.models import User
'''from tinymce import TinyMCE'''
from .models import Event
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
class EventForm(forms.ModelForm):
	class Meta():
		model=Event
		fields = ('category', 'name', 'venue', 'time', 'date','num_of_attendees',)