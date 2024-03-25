from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django import forms
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# def landing_page(request):
#     template_name = 'landing_page/landing_page.html'
#     return render(request, template_name)

class LandingView(generic.TemplateView):
    """
    Rendered HTML file, no backend impact
    """
    template_name = 'landing_page/landing_page.html'
    context_object_name = 'landing_page'

class LoginView(LoginView):
    """
    This is necessary for all users who want to use skill scout, 
    login queries the database for a valid login credential, 
    LoginView import naturally will do this, no need to do anything.
    """
    template_name = 'landing_page/login.html'
    success_url = reverse_lazy('landing_page:landing_page')

class ExtendedSignupForm(UserCreationForm):
    """
    Creates additional fields for the signup of a new user.
    """
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class SignupView(FormView):
    """
    This View will query the user to make a username and input things such as their email and name and will then set it in the backend as a user
    """
    template_name = 'landing_page/signup.html'
    form_class = ExtendedSignupForm
    success_url = reverse_lazy('landing_page:login')


    def form_valid(self, form):
        user = form.save()
        group = form.cleaned_data['group']
        user.groups.add(group)
        messages.success(self.request, 'Your account has been created successfully.')
        return super().form_valid(form)



def redirect_to_jobbot_talent(request):
    """
    goes to the other app parsonsjobbot, jobbot:name will query the whole project for a name corresponding
    """
    return redirect('jobbot:home')

def redirect_to_jobbot_resume(request):
    """
    goes to the other app parsonsjobbot, jobbot:name will query the whole project for a name corresponding
    """
    return redirect('jobbot:resume-home')

def redirect_to_jobbot_about(request):
    """
    goes to the other app parsonsjobbot, jobbot:name will query the whole project for a name corresponding
    """
    return redirect('jobbot:about')

def redirect_to_jobbot_profile(request):
    """
    goes to the other app parsonsjobbot, jobbot:name will query the whole project for a name corresponding
    """
    return redirect('jobbot:profile')


