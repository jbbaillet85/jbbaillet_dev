from apps.project.models import Project
from django import forms


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
        ]
        help_texts = {
            'name': 'Le nom de project',
        }
