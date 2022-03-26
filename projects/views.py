from audioop import reverse
from re import template
from unicodedata import category
from django.shortcuts import render, reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm, CreateProjectForm, UpdateProjectForm
from .models import Project
from .services import create_project

# Create your views here.


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('login')


class LandingPage(generic.TemplateView):
    template_name = 'landing-page.html'


class ProjectCreateView(LoginRequiredMixin, generic.FormView):
    template_name = 'project-create.html'
    form_class = CreateProjectForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        project = create_project(self.request, form_data)
        if not project:
            messages.add_message(self.request, messages.INFO,
                                 message='You already have a project by this name')
            return self.form_invalid(form)

        return super(ProjectCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projects:project-list")


class ProjectListView(generic.ListView):
    template_name = 'project-list.html'
    context_object_name = "projects"

    def get_queryset(self):
        user = self.request.user
        query_set = Project.objects.filter(
            owner=self.request.user
        )
        return query_set


class ProjectDetailView(generic.DetailView):
    template_name = "project-detail.html"
    context_object_name = "project"

    model = Project


class ProjectUpdateView(generic.UpdateView):
    success_url = 'projects:project-detail'
    template_name = 'project-create.html'
    model = Project
    form_class = UpdateProjectForm

    def get_success_url(self) -> str:
        if self.kwargs['slug']:
            slug = self.kwargs['slug']
            return reverse('projects:project-detail', args=(slug,))
        return reverse('projects:project-list')


class ProjectDeleteView(generic.DeleteView):
    template_name = 'project-delete.html'

    def get_success_url(self):
        return reverse('projects:project-list')
    model = Project
    pass


class TicketCreateView(generic.CreateView):
    pass


class TicketListView(generic.ListView):
    pass


class TicketDetailView(generic.DetailView):
    pass


class TicketUpdateView(generic.UpdateView):
    pass


class TicketDeleteView(generic.DeleteView):
    pass
