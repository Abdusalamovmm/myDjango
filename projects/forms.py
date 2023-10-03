from django import forms
from .models import Project, Student

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['student', 'title', 'annotation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].widget.attrs.update({
            'class': 'form-select',
            'id': 'student-select'
        })
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'title-input',
            'placeholder': 'Введите название проекта'
        })
        self.fields['annotation'].widget.attrs.update({
            'class': 'form-control',
            'id': 'annotation-textarea',
            'placeholder': 'Введите аннотацию проекта'
        })

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'email', 'phone', 'passport']
