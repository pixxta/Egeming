from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import TaskForm
from .models import Task





def home_page(request):
    """Начальная страница - тестовая"""

    return HttpResponse("Начальная страница")


def react_page(request):
    """Тестовая страница для реакта"""

    return render(request, 'react_page.html')


class TaskView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        task_data = [{'subject_type' : task.subject_type, 'task_number' : task.task_number, 'title': task.title, 'task_condition': task.task_condition, 'points': task.points} for task in tasks]
        return JsonResponse({'tasks': task_data}, safe=False)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Task added successfully'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

class TaskListView(View):
    template_name = 'task_list.html'

    def get(self, request, *args, **kwargs):
        subject_type_filter = request.GET.get('subject_type', '')  # Получаем значение subject_type из GET-параметра
        tasks = Task.objects.all()
        
        if subject_type_filter:  # Если subject_type указан, фильтруем задачи
            tasks = tasks.filter(subject_type=subject_type_filter)
            
        return render(request, self.template_name, {'tasks': tasks, 'subject_type_filter': subject_type_filter})
    
    
# Добавляем новое представление для создания задания
class CreateTaskView(View):
    template_name = 'create_task.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)