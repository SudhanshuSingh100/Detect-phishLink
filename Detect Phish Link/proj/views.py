from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from proj.models import Task
from proj.tasks import my_task

def create_task(request):
    if request.method == 'GET':
        return render(request, 'proj/new_task.html')
    if request.method == 'POST':
        url = request.POST['url']
        new_task = Task.objects.create(url=url)
        my_task.delay(new_task.id)
        return redirect(reverse('status', args=[new_task.id]))

    return HttpResponse(status=405)

def get_task_status(request, task_id):
    if request.method != 'GET':
        return HttpResponse(status=405)
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return render(request, 'proj/invalid_task.html')

    if task.processed:
        return render(request, 'proj/processed.html', {'result': task.result})
    else:
        return render(request, 'proj/wait.html')
