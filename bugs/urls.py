from django.urls import path
from . import views

urlpatterns = [
    path('', views.BugListView.as_view(), name='bug-list'),
    path('bug/new/', views.BugCreateView.as_view(), name='bug-create'),
    path('bug/<int:pk>/', views.BugDetailView.as_view(), name='bug-detail'),
    path('bug/<int:pk>/edit/', views.BugUpdateView.as_view(), name='bug-update'),
    path('bug/<int:pk>/status/', views.update_bug_status, name='update-bug-status'),
]