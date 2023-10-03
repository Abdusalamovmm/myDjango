from django.http import HttpResponse, Http404
from .models import Project, Student
from .forms import ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .forms import StudentForm


# Представление для отображения списка проектов
def index(request):
    # Получаем все объекты модели Project из базы данных
    projects = Project.objects.all()
    # Рендерим шаблон index.html с передачей списка проектов в контекст
    return render(request, "projects/index.html", {"projects": projects})

# Представление для отображения детальной информации о проекте по его идентификатору
def detail(request, pk):
    # Получаем объект модели Project по его идентификатору или возвращаем 404 ошибку, если такого объекта нет
    project = get_object_or_404(Project, pk=pk)
    # Рендерим шаблон detail.html с передачей объекта проекта в контекст
    return render(request, "projects/detail.html", {"project": project})

# Представление для создания нового проекта
def create(request):
    # Если запрос методом POST, то обрабатываем данные из формы
    if request.method == "POST":
        # Создаем объект формы ProjectForm с данными из запроса
        form = ProjectForm(request.POST)
        # Проверяем валидность данных в форме
        if form.is_valid():
            # Сохраняем данные из формы в базу данных
            form.save()
            # Перенаправляем пользователя на главную страницу со списком проектов
            return redirect("index")
    # Если запрос методом GET, то отображаем пустую форму для ввода данных
    else:
        # Создаем объект пустой формы ProjectForm
        form = ProjectForm()
    # Рендерим шаблон create.html с передачей объекта формы в контекст
    return render(request, "projects/create.html", {"form": form})

# Представление для редактирования существующего проекта по его идентификатору
def update(request, pk):
    # Получаем объект модели Project по его идентификатору или возвращаем 404 ошибку, если такого объекта нет
    project = get_object_or_404(Project, pk=pk)
    # Если запрос методом POST, то обрабатываем данные из формы
    if request.method == "POST":
        # Создаем объект формы ProjectForm с данными из запроса и объекта проекта
        form = ProjectForm(request.POST, instance=project)
        # Проверяем валидность данных в форме
        if form.is_valid():
            # Сохраняем изменения в базе данных
            form.save()
            # Перенаправляем пользователя на страницу с детальной информацией о проекте
            return redirect("detail", pk=pk)
    # Если запрос методом GET, то отображаем форму с данными объекта проекта для редактирования
    else:
        # Создаем объект формы ProjectForm с данными объекта проекта
        form = ProjectForm(instance=project)
    # Рендерим шаблон update.html с передачей объекта формы и объекта проекта в контекст
    return render(request, "projects/update.html", {"form": form, "project": project})

# Представление для удаления проекта по его идентификатору
def delete(request, pk):
    # Получаем объект модели Project по его идентификатору или возвращаем 404 ошибку, если такого объекта нет
    project = get_object_or_404(Project, pk=pk)
    # Если запрос методом POST, то удаляем объект проекта из базы данных
    if request.method == "POST":
        project.delete()
        # Перенаправляем пользователя на главную страницу со списком проектов
        return redirect("index")
    # Если запрос методом GET, то отображаем страницу с подтверждением удаления проекта
    else:
        # Рендерим шаблон delete.html с передачей объекта проекта в контекст
        return render(request, "projects/delete.html", {"project": project})
