from .models import Project
from django.template.defaultfilters import slugify


def create_project(request, project):
    project_name = project['name']
    project_description = project['description']
    project_slug = slugify(project_name)
    project_owner = request.user

    if Project.objects.filter(owner=project_owner, name=project_name):
        return None

    project = Project(name=project_name, description=project_description,
                      slug=project_slug, owner=project_owner)
    project.save()
    return project
