from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'severity', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }