from django.shortcuts import render, redirect
from .models import Task
from .models import Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .ai_api import send_request


# Create your views here.
@login_required
def list_tasks(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.prefetch_related('answer_set')
    user_info = request.user
    print(user_info)
    return render(request, "list_tasks.html", {
        "tasks": tasks,
        "user_info" : user_info,
    })

@login_required
def list_task_user(request):
    tasks = Task.objects.filter(created_by=request.user).prefetch_related('answer_set')
    user_info = request.user
    print(user_info)
    return render(request, "list_tasks_user.html", {
        "tasks": tasks,
        "user_info" : user_info,
    })
@login_required
def create_task(request):
    new_input = request.POST["input_value"]
    user = request.user
    # new_description = request.POST["description"]
    if new_input == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html",
            {"tasks": tasks,
             "error": "No seas timido, introduzce alguna pregunta..."}
        )
    task = Task(input_value=new_input, created_by=user)
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
        answer = Answer(answer_value=ai_response, task=task)
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

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")


def home(request):
    user_info = request.user
    return render(request, 'index.html', {
          "user_info": user_info,
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe!'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password no son iguales!'
        })


def base(request):
    return render(request, 'base.html')


def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',
                      {
                          'form': AuthenticationForm
                      })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',
                          {
                              'form': AuthenticationForm,
                              'error': 'Usuario o contraseña incorrectos'
                          })
        else:
            login(request, user)
            return redirect('index')
