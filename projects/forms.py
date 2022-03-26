from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import Project
User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}


class CreateProjectForm(forms.Form):
    name = forms.CharField(label='Project name',
                           max_length=120)
    description = forms.CharField(
        label='Project description', widget=forms.Textarea, required=False)


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'description']
