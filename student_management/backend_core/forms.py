from django import forms

from backend_core.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = [
            "id"
        ]