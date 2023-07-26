from apps.project.models import Project
from apps.project.forms import ProjectForm
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView, ListView)

class ProjectCreateView(CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = ProjectForm


class <built-in method title of str object at 0x7f44ccc4b8f0>UpdateView(UpdateView):
    model = Project
    template_name = "project/update_project.html"
    form_class = ProjectForm


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/delete_project.html"
    success_url = "/"  # Rediriger vers l'URL souhaitée après la suppression


class <built-in method title of str object at 0x7f44ccc4b8f0>DetailView(DetailView):
    model = <built-in method title of str object at 0x7f44ccc4b8f0>
    template_name = "project/detail_project.html"


class ProjectListView(ListView):
    model = Project
    template_name = "project/list_project.html"
