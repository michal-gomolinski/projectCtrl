from audioop import reverse
from re import template
from django.shortcuts import render, reverse
from django.views import generic
from .forms import CreateUserForm

# Create your views here.


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('login')


class LandingPage(generic.TemplateView):
    template_name = 'landing-page.html'


class ProjectCreateView(generic.CreateView):
    pass


class ProjectListView(generic.ListView):
    pass


class ProjectDetailView(generic.DetailView):
    pass


class ProjectUpdateView(generic.UpdateView):
    pass


class ProjectDeleteView(generic.DeleteView):
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
