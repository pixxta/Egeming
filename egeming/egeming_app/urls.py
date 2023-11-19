from django.urls import path
from . import views
from .views import TaskListView, CreateTaskView

urlpatterns = [
    path('', views.home_page),
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('create-task/', CreateTaskView.as_view(), name='create_task'),

]