from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.TaskListView.as_view(), name='task_list'),
    path('api/report/', views.ReportView.as_view(), name='report'),
]
