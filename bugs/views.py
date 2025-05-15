from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Bug
from .forms import BugForm

class BugListView(ListView):
    model = Bug
    template_name = 'bugs/bug_list.html'
    context_object_name = 'bugs'
    
    def get_queryset(self):
        queryset = Bug.objects.all()
        
        # Filter by severity
        severity = self.request.GET.get('severity')
        if severity:
            queryset = queryset.filter(severity=severity)
            
        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['severity_choices'] = Bug.SEVERITY_CHOICES
        context['status_choices'] = Bug.STATUS_CHOICES
        return context

class BugCreateView(CreateView):
    model = Bug
    form_class = BugForm
    template_name = 'bugs/bug_form.html'
    success_url = reverse_lazy('bug-list')

class BugUpdateView(UpdateView):
    model = Bug
    form_class = BugForm
    template_name = 'bugs/bug_form.html'
    success_url = reverse_lazy('bug-list')

class BugDetailView(DetailView):
    model = Bug
    template_name = 'bugs/bug_detail.html'
    context_object_name = 'bug'

def update_bug_status(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status and new_status in dict(Bug.STATUS_CHOICES):
            bug.status = new_status
            bug.save()
    
    return redirect('bug-detail', pk=bug.pk)
