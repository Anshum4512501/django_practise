from django.shortcuts import render,reverse
from django.views.generic import CreateView,ListView,DetailView,DeleteView,TemplateView,UpdateView
from .models import School
from .forms import CreateSchoolForm,CreateStudentForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# class CreateSchool(CreateView):
#     model = School
#     # queryset = School.objects.all()
#     fields = ('name','location','principal')
#     # template_name = 'school/school_form.html'
   

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'school/school_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_school'] = School.objects.all()
        return context

class CreateSchool(LoginRequiredMixin,CreateView):
    form_class = CreateSchoolForm
    # queryset = School.objects.all()
    
    template_name = 'school/school_form.html'

class CreateSchoolStudent(LoginRequiredMixin,CreateView):
    form_class = CreateStudentForm
    # queryset = School.objects.all()
    
    template_name = 'school/school_form.html'

class SchoolList(LoginRequiredMixin,ListView):
    # queryset = School.objects.all()
    context_object_name = 'schools'
    model = School
    # def get_queryset(self):
    #     instance = super().get_queryset()
    #     print(instance)
    #     return instance
    

class SchoolDetailView(LoginRequiredMixin,DetailView):
    model = School
    context_object_name = 'school'


class SchoolUpdateView(LoginRequiredMixin,UpdateView):
    form_class = CreateSchoolForm
    model = School
    context_object_name = 'school'
    template_name = 'school/school_form.html'



class SchoolDeleteView(DeleteView):
    model =School
    
    def get_success_url(self):
        return reverse('school:school_list')