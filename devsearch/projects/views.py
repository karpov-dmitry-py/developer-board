from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Project
from .models import Tag


# noinspection PyUnresolvedReferences
def get_projects(request):
    projects = Project.objects.prefetch_related('tags').all()
    reviews = {project.id: [rev.value for rev in project.reviews.all()] for project in
               Project.objects.prefetch_related('reviews').all()}
    tags = Tag.objects.prefetch_related('projects').all()
    ctx = {
        'projects': projects,
        'tags': tags,
        'reviews': reviews,
    }
    return render(request=request, template_name='projects/projects.html', context=ctx)


def get_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    ctx = {'project': project}
    return render(request=request, template_name='projects/single-project.html', context=ctx)
