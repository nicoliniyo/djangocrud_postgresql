from django.shortcuts import render, redirect
from .models import Task
from .models import Answer
from .constants import default_engine

from .ai_api import send_request
# Create your views here.
def list_tasks(request):
    # tasks = Task.objects.all()
    tasks =  Task.objects.prefetch_related('answer_set')
    return render(request, "list_tasks.html", {"tasks": tasks})


def create_task(request):
    new_input = request.POST["input_value"]
    # new_description = request.POST["description"]
    if new_input == "" :
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html",
            {"tasks": tasks,
             "error": "Title and description is required"}
        )
    task = Task(input_value=new_input)
    task.save()
    ai_response = send_request(new_input)
    answer = Answer(answer_value = ai_response, task = task)
    answer.save()
    print(ai_response)
    return redirect("/tasks/")


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")
