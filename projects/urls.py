from django.urls import path, include
from .views import LandingPage, ProjectCreateView, ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

app_name = 'projects'

urlpatterns = [
    path('', LandingPage.as_view(), name="landing-page"),
    path('project-create/', ProjectCreateView.as_view(), name="project-create"),
    path('project-list/', ProjectListView.as_view(), name="project-list"),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<slug:slug>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('<slug:slug>/delete', ProjectDeleteView.as_view(), name='project-delete'),
]
