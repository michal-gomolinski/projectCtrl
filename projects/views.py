from django.shortcuts import render
from django.views import generic


# Create your views here.
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