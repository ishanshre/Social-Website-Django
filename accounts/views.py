from django.shortcuts import render, redirect
from django.views.generic.edit import (
    CreateView,
    DeleteView,
)
from django.views import View
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginViewForm, CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    message = 'Account Created Successfully'
    success_url = reverse_lazy('accounts:login')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('images:index')
        return super(SignUpView,self).dispatch(request,*args,**kwargs)

class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginViewForm
    template_name = 'accounts/login.html'
    message = "Login Success"

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message


class UserPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('images:index')
    message = 'Password Change Successfull'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    

class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    message = 'Reset Link has been sent to your email address. If not, then try again with correct email address'
    success_url = reverse_lazy('accounts:login')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('images:index')
        return super(UserPasswordResetView, self).dispatch(request,*args, **kwargs)

class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('images:index')
    message = 'Password Reset Successfull'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('images:index')
        return super(UserPasswordResetConfirmView, self).dispatch(request,*args,**kwargs)
    


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(request, self.template_name, context={'profile':profile})
    
        
    
class ProfileUpdateView(SuccessMessageMixin,LoginRequiredMixin, View):
    template_name = 'accounts/profile_update.html'
    message = 'Profile Updated'
    def get(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, context={'user_form':user_form,'profile_form':profile_form})
    
    def post(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES ,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, self.message)
            return redirect('accounts:user_profile')
        else:
            user_form = CustomUserChangeForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, context={'user_form':user_form,'profile_form':profile_form})


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'accounts/delete_user.html'
    message = 'Account Closed'
    success_url = reverse_lazy('images:index')

    def get_object(self):
        return self.model.objects.get(id=self.kwargs['pk'])

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message