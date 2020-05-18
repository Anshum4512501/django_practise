from django import forms
from .models import School,Student


class CreateSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name','location','principal')


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','school')


