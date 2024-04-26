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
             "error": "No seas timido, introduzce alguna pregunta..."}
        )
    task = Task(input_value=new_input)
    task.save()
    try:
        print('SENDING QUERY TO LLM:')
        ai_response = send_request(new_input)
        print('LLM RESPONSE:')
        print(ai_response)
        if ai_response == "":
            tasks = Task.objects.all()
            return render(
                request, "list_tasks.html",
                {"tasks": tasks,
                 "error": "Hubo un error, no pude recolectar la respuesta..."}
            )
        answer = Answer(answer_value = ai_response, task = task)
        answer.save()
        print(ai_response)
        return redirect("/tasks/")
    except (KeyError, ValueError) as e:
        tasks = Task.objects.all()
        print(KeyError)
        print(ValueError)
        return render(
            request,
            "list_tasks.html",
            {"tasks": tasks, "error": f"Error: {str(e)}"},
        )



def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")
