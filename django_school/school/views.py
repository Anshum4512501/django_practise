from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .models import School
from .forms import CreateSchoolForm,CreateStudentForm
# Create your views here.


# class CreateSchool(CreateView):
#     model = School
#     # queryset = School.objects.all()
#     fields = ('name','location','principal')
#     # template_name = 'school/school_form.html'
   

class CreateSchool(CreateView):
    form_class = CreateSchoolForm
    # queryset = School.objects.all()
    
    template_name = 'school/school_form.html'

class CreateSchoolStudent(CreateView):
    form_class = CreateStudentForm
    # queryset = School.objects.all()
    
    template_name = 'school/school_form.html'

class SchoolList(ListView):
    queryset = School.objects.all()
    context_object_name = 'schools'
    

class SchoolDetailView(DetailView):
    model = School
    context_object_name = 'school'