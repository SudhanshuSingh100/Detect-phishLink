from proj.celery import app
from proj.detection.MainPhishing import process
from proj.models import Task

@app.task
def my_task(task_id):
    task = Task.objects.get(id=task_id)
    try:
        result = process(task.url)
    except Exception:
        task.result = 'Please try again!'
    else:
        task.result = result
    finally:
        task.processed = True
        task.save()
