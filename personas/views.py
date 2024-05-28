from django.shortcuts import render, redirect
from .models import Persona
from .models import PersonaForm

def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html',
                  {'form': form,
                   'error' : form.errors
                   })

def persona_update(request, pk):
    persona = Persona.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def persona_delete(request, pk):
    persona = Persona.objects.get(pk=pk)
    persona.delete()
    return redirect('persona_list')
