from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proyecto, Tarea
from .forms import RegistroForm, ProyectoForm, TareaForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f"¡Bienvenido {usuario.username}!")
            return redirect('lista_proyectos')
    else:
        form = RegistroForm()
    return render(request, 'api/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('lista_proyectos')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'api/login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'api/proyecto_lista.html', {'proyectos': proyectos})


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            messages.success(request, "Proyecto creado")
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'api/proyecto_form.html', {'form': form})


@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto actualizado")
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'api/proyecto_form.html', {'form': form})


@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, "Proyecto eliminado")
        return redirect('lista_proyectos')
    return render(request, 'api/proyecto_confirmar_eliminar.html', {'proyecto': proyecto})


@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(proyecto__usuario=request.user)
    return render(request, 'api/tarea_lista.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, usuario=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea creada")
            return redirect('lista_tareas')
    else:
        form = TareaForm(usuario=request.user)
    return render(request, 'api/tarea_form.html', {'form': form})


@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, proyecto__usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea, usuario=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea actualizada")
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea, usuario=request.user)
    return render(request, 'api/tarea_form.html', {'form': form})


@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, proyecto__usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, "Tarea eliminada")
        return redirect('lista_tareas')
    return render(request, 'api/tarea_confirmar_eliminar.html', {'tarea': tarea})