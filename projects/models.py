from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Модель студента
class Student(models.Model):
    # Поля модели
    name = models.CharField(max_length=100) # Имя студента
    course = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], error_messages={'min_value': 'Курс должен быть больше или равен 1', 'max_value': 'Курс должен быть меньше или равен 4'})
    email = models.EmailField() # Электронная почта
    phone = models.CharField(max_length=20) # Телефон
    passport = models.CharField(max_length=10) # Паспорт


    # Метод для получения строкового представления объекта модели
    def __str__(self):
        return self.name

# Модель для хранения информации о проекте
class Project(models.Model):
    # Поля модели
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # Ссылка на студента, выполняющего проект
    title = models.CharField(max_length=200) # Название проекта
    annotation = models.TextField() # Аннотация проекта

    # Метод для получения строкового представления объекта модели
    def __str__(self):
        return self.title

