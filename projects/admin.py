from django.contrib import admin
from .models import Project, Student

# Класс для настройки отображения модели Project в административной панели
class ProjectAdmin(admin.ModelAdmin):
    # Список полей, которые будут отображаться в таблице проектов
    list_display = ('title', 'student', 'annotation')
    # Список полей, по которым можно осуществлять поиск
    search_fields = ('title', 'student__name')
    # Список полей, по которым можно фильтровать проекты
    list_filter = ('student',)

# Класс для настройки отображения модели Student в административной панели
class StudentAdmin(admin.ModelAdmin):
    # Список полей, которые будут отображаться в таблице студентов
    list_display = ('name', 'course', 'email', 'phone', 'passport')
    # Список полей, по которым можно осуществлять поиск
    search_fields = ('name', 'email')
    # Список полей, по которым можно фильтровать студентов
    list_filter = ('course',)

# Регистрируем модели и их классы настройки в административной панели
admin.site.register(Project, ProjectAdmin)
admin.site.register(Student, StudentAdmin)
