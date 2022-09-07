from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile
from django_countries.widgets import CountrySelectWidget


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['first_name','last_name','age','username','email']
    
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta():
        model = get_user_model()
        fields = ['first_name','last_name','age','username','email']
    
class LoginViewForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(max_length=255, label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    remember_me = forms.BooleanField(required=False)
    class Meta:
        model = get_user_model()
        fields = ['username','password','remember_me']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo','bio', 'country']
        widgets = {
            'country': CountrySelectWidget()   
        }